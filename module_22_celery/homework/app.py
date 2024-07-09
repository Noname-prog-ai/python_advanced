"""
В этом файле будет ваше Flask-приложение
"""

from flask import Flask, request
from image import blur_image
from mail import send_email
import sqlite3

app = Flask(__name__)

# Создаем базу данных для хранения подписчиков
conn = sqlite3.connect('subscribers.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS subscribers (email text primary key)''')

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
    c.execute("INSERT INTO subscribers (email) VALUES (?)", (email,))
    conn.commit()
    return {'message': 'subscribed successfully'}

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    email = request.form.get('email')
    c.execute("DELETE FROM subscribers WHERE email = ?", (email,))
    conn.commit()
    return {'message': 'unsubscribed successfully'}

if __name__ == '__main__':
    app.run(debug=True)
