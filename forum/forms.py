from django.shortcuts import redirect, render
from django_ckeditor_5.widgets import CKEditor5Widget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
from django import forms
from rest_framework import request

from .models import *


class LikeForm(forms.ModelForm):
    class Meta:
        model = CommentLike
        fields = [
            "comment",
            "user",
        ]


class RatingForm(forms.ModelForm):
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=[(i, i) for i in range(1, 11)])
    class Meta:
        model = PostRating
        fields = '__all__'


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Comment
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





