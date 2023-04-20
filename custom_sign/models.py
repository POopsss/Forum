from django.db import models
from forum.tasks import task_starter
from allauth.account.models import EmailAddress


class EmailVerified(models.Model):
    password = models.IntegerField()
    email = models.OneToOneField(EmailAddress, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def email_verified(self):
        mail = {
            'to': [self.email.email],
            'subject': 'Код подтверждения',
            'text': f'Код подтверждения {self.password}',
            'html': f'Введите код подтверждения {self.password} по <a href="http://127.0.0.1:8000/account/verified/?mail={self.email}">ссылке</a>',
        }
        task_starter(mail)

