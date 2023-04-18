from allauth.account.forms import SignupForm
from forum.models import FUser
from django import forms


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        return user


class UserForm(forms.ModelForm):
    class Meta:
        permission_required = ('forum.change_fuser',)
        model = FUser
        fields = ['name', 'avatar']
