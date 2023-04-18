from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

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
    title = forms.CharField()
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label='Категории')

    class Meta:
        model = Post
        fields = ('title', 'category', 'text',)
