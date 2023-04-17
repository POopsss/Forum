from celery import shared_task
from django.core.mail import EmailMultiAlternatives


@shared_task
def mail_sender(mail):
    msg = EmailMultiAlternatives(
        subject=mail.get('subject'), body=mail.get('text'), from_email=None, to=mail.get('to')
    )
    msg.attach_alternative(mail.get('html'), "text/html")
    msg.send()


@shared_task
def post_created(instance_id):
    pass