from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.generic import UpdateView
from forum.models import *
from .forms import UserForm
from django.contrib.auth.models import User


def user(request):
    template_name = "user.html"
    if request.user.is_anonymous:
        return redirect('/accounts/login/')
    context = {
        'user': FUser.objects.get(email=request.user),
    }
    return render(request, template_name, context)



# class UserUpdate(PermissionRequiredMixin, UpdateView):
#     permission_required = ('accounts.user',)
#     form_class = UserForm
#     model = FUser
#     template_name = 'user_edit.html'