from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.generic import UpdateView
from forum.models import FUser, Post
from .forms import UserForm
from django.contrib.auth.models import User


def user(request):
    template_name = "user.html"
    if request.user.is_anonymous:
        return redirect('/accounts/login/')
    fuser = FUser.objects.get(email=request.user)
    context = {
        'user': fuser,
        'user_form': UserForm,
    }
    if request.method == 'POST':
        if request.POST.get('posttype') == 'name':
            fuser.name = request.POST.get('name')
        if request.POST.get('posttype') == 'avatar':
            file = request.FILES['avatar']
            fs = FileSystemStorage()
            avatar = fs.save(file.name, file)
            fuser.avatar = avatar
        fuser.save()
        return redirect('user')
    return render(request, template_name, context)


def user_post(request):
    template_name = "user_post.html"
    if request.user.is_anonymous:
        return redirect('/accounts/login/')
    fuser = FUser.objects.get(email=request.user)
    user_post = Post.objects.all().filter(author=fuser)
    context = {
        'user': fuser,
        'user_post': user_post,
    }
    return render(request, template_name, context)

