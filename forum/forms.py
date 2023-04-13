from django_ckeditor_5.widgets import CKEditor5Widget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import *


class ResponseForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Response
        fields = '__all__'


class PostForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=FUser.objects.all(),
                                    initial=FUser.objects.all()[0],
                                    widget=forms.HiddenInput()
                                    )
    title = forms.CharField()
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label='Категории')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].required = False

    class Meta:
        model = Post
        fields = ('author', 'title', 'category', 'text',)
        widgets = {
            'text': CKEditor5Widget(
                attrs={'class': 'django_ckeditor_5'}, config_name='extends'
            ),
        }





