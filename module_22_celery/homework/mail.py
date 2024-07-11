import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from config import smtp_host, smtp_port, smtp_password, smtp_user

def send_email(receiver, filename):
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)

        email = MIMEMultipart()
        email['Subject'] = 'Subject'
        email['From'] = smtp_user
        email['To'] = receiver

        with open(filename, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={filename}')
        email.attach(part)
        text = email.as_string()

        server.sendmail(smtp_user, receiver, text)