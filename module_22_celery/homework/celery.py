"""
В этом файле будут Celery-задачи
"""

from mail import send_email
from celery import Celery
from image import blur_image
from mail import send_email
from config import smtp_host, smtp_port, smtp_password, smtp_user
from modules import zip_path, get_all_email, get_group_id, image_to_zip
from celery.schedules import crontab

celery = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@celery.task
def process_image(image_name: str):
    """
    процесс обработки изображений
    """
    blur_image(src_filename=image_name)

    return f"image name: {image_name} processed"

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    процесс подготовки еженедельного информационного бюллетеня
    """
    sender.add_periodic_task(
        crontab(hour=12, minute=30, day_of_week=1),
        subscribe_email.s()
    )

@celery.task
def subscribe_email():
    """
    процесс отправки еженедельных информационных бюллетеней по электронной почте
    """
    mail_list = get_all_email()
    if mail_list:
        for i_mail in mail_list:
            send_email(receiver=i_mail)

@celery.task
def send_email_zip(email: str, image_names: list, record_id: int):
    """
    процесс отправки заархивированных изображений по электронной почте
    """