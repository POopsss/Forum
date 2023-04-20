from celery import shared_task
from django.core.mail import EmailMultiAlternatives


def task_starter(mail):
    mail_sender.delay(mail)
    # mail_sender(mail)
    # pass


@shared_task
def mail_sender(mail):
    msg = EmailMultiAlternatives(
        subject=mail.get('subject'), body=mail.get('text'), from_email=None, to=mail.get('to')
    )
    msg.attach_alternative(mail.get('html'), "text/html")
    msg.send()
