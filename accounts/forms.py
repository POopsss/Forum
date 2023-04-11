from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives
from forum.models import FUser
from django import forms


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
#         # user.groups.add(Group.objects.get(name='common users'))
        subject = 'Добро пожаловать на 127.0.0.1:8000!'
        text = f'{user.username}, вы успешно зарегистрировались на сайте!'
        html = (
            f'<b>{user.username}</b>, вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000/">сайте</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()
        return user


class UserForm(forms.ModelForm):
    class Meta:
        permission_required = ('forum.change_fuser',)
        model = FUser
        # print(FUser)
        fields = ['name', 'avatar']