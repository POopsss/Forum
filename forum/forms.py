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
        response = super().save(self)
        Response.new_response(response)

        return response


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
