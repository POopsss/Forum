from forum.models import FUser
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        permission_required = ('forum.change_fuser',)
        model = FUser
        fields = ['name', 'avatar']
