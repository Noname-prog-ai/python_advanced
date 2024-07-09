"""
В этом файле будет ваше Flask-приложение
"""

from flask import Flask, request
from image import blur_image
from mail import send_email

app = Flask(__name__)

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
    # Здесь будет логика подписки, пока просто возвращаем успешное сообщение
    return {'message': 'subscribed successfully'}

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    email = request.form.get('email')
    # Здесь будет логика отписки, пока просто возвращаем успешное сообщение
    return {'message': 'unsubscribed successfully'}

if __name__ == '__main__':
    app.run(debug=True)
