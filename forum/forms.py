from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib.sites import requests
from django.core.mail import EmailMultiAlternatives

from .models import *


class ResponseForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Response
        fields = '__all__'

    def save(self):
        resp = super().save(self)
        print(self.data.get('author').name)
        print(self.data.get('post').author.email.email)
        print(self.data.get('text'))
        print(self.data.get('post').title)

        subject = 'Вам пришёл отклик на объявление'
        text = f'{self.data.get("author").name}, оставил отклик на ваше объявление: {self.data.get("post").title}'
        html = f'{self.data.get("author").name}, оставил отклик: {self.data.get("text")} на ваше объявление: {self.data.get("post").title}'
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[self.data.get('post').author.email.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        return resp


class PostForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=FUser.objects.all(),
                                    initial=FUser.objects.all()[0],
                                    widget=forms.HiddenInput()
                                    )
    title = forms.CharField()
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label='Категории')


    class Meta:
        model = Post
        fields = ('author', 'title', 'category', 'text',)
