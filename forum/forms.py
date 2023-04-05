from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms

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
    # text = forms.Textarea()
    class Meta:
        model = Comment
        fields = '__all__'


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = ['text',
                  ]



