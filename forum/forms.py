from django import forms
from .models import *


class LikeForm(forms.ModelForm):
    class Meta:
        model = CommentLike
        fields = '__all__'


class RatingForm(forms.ModelForm):
    class Meta:
        model = PostRating
        fields = '__all__'