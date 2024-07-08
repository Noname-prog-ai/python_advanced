"""
В этом файле будет ваше Flask-приложение
"""

from flask import Flask, request
from celery import Celery
from image import blur_image
from mail import send_email

app = Flask(__name__)
celery = Celery(app.import_name, broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@celery.task
def process_image(email, filename):
    blurred_filename = blur_image(filename)
    send_email(email, blurred_filename)

@app.route('/blur', methods=['POST'])
def blur_images():
    images = request.files.getlist('images')
    email = request.form.get('email')

    task_ids = []

    for image in images:
        task = process_image.delay(email, image.filename)
        task_ids.append(task.id)

    return {'task_ids': task_ids}

@app.route('/status/<task_id>', methods=['GET'])
def task_status(task_id):
    task = process_image.AsyncResult(task_id)

    if task.successful():
        return {'status': 'completed'}
    else:
        return {'status': 'processing'}

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')

    return {'message': 'Subscribed successfully'}

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    email = request.form.get('email')

    return {'message': 'Unsubscribed successfully'}

if __name__ == '__main__':
    app.run(debug=True)
