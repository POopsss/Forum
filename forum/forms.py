from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import *


class ReplyForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Reply
        fields = '__all__'

    def save(self):
        reply = super().save(self)
        Reply.new_reply(reply)

        return reply


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок')
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label='Категории')

    class Meta:
        model = Post
        fields = ('title', 'category', 'text',)

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = 'Содержание'


