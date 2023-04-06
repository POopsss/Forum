from django_ckeditor_5.widgets import CKEditor5Widget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
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
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Comment
        fields = '__all__'


# class CommentForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["text"].required = False
#
#
#     class Meta:
#         model = Comment
#         fields = [
#             'text',
#         ]
#         widgets = {
#             "text": CKEditor5Widget(
#                 attrs={"class": "django_ckeditor_5"}, config_name='default'
#             )
#         }


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(config_name='default'))
    class Meta:
        model = Post
        fields = ['text',]



