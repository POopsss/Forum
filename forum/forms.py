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
    rating = forms.IntegerField(max_value=10, min_value=1)
    class Meta:
        model = PostRating
        fields = '__all__'