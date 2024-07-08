"""
В этом файле будут Celery-задачи
"""

from celery import Celery
from image import blur_image
from mail import send_email
from config import smtphost, smtpport, smtppassword, smtpuser

celery = Celery(__name__, broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@celery.task
def process_image(email, filename):
    blurred_filename = blur_image(filename)
    send_email(email, blurred_filename)