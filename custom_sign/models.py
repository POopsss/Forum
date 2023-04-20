from django.db import models
from django.contrib.auth.models import User
from forum.tasks import mail_sender
from allauth.account.models import EmailAddress


class EmailVerified(models.Model):
    password = models.IntegerField(unique=True)
    email = models.ForeignKey(EmailAddress, on_delete=models.CASCADE)

    def email_verified(self):
        mail = {
            'to': [self.email.email],
            'subject': 'Код подтверждения',
            'text': f'Код подтверждения {self.password}',
            'html': f'Введите код подтверждения {self.password} по <a href="http://127.0.0.1:8000/qwe/verified">ссылке</a>',
        }
        mail_sender.delay(mail)

