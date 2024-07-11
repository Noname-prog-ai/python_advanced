"""
В этом файле будет ваше Flask-приложение
"""

from flask import Flask, request
from image import blur_image
from mail import send_email
from celery import Celery
import sqlite3

app = Flask(__name__)

# Создаем базу данных для хранения подписчиков
conn = sqlite3.connect('subscribers.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS subscribers (email text primary key)''')

# Инициализируем Celery для выполнения задач
celery = Celery(__name__, broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@celery.task
def process_image(email, filename):
    """Функция для обработки изображения и отправки почты"""
    blurred_filename = blur_image(filename)
    send_email(email, blurred_filename)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Маршрут для подписки на рассылку"""
    email = request.form.get('email')
    c.execute("INSERT INTO subscribers (email) VALUES (?)", (email,))
    conn.commit()
    return {'message': 'subscribed successfully'}

# Добавляем периодическую задачу для рассылки новостей
@celery.task(name='send_newsletter')
def send_newsletter():
    """Функция для отправки писем подписчикам с рассылкой"""
    subscribers = c.execute("SELECT email FROM subscribers").fetchall()
    for subscriber in subscribers:
        process_image.delay(subscriber[0], 'newsletter_image.jpg')

if __name__ == '__main__':
    app.run(debug=True)