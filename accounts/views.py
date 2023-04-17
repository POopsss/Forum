from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from forum.models import FUser, Post, Response
from .forms import UserForm
from django.core.paginator import Paginator
from forum.filters import PostFilter, ResponseFilter
from forum.tasks import *


def user(request):
    template_name = "user.html"
    if request.user.is_anonymous:
        return redirect('/accounts/login/')
    fuser = FUser.objects.get(email=request.user)
    if request.method == 'GET':
        context = {
            'user': fuser,
            'user_form': UserForm,
        }
        return render(request, template_name, context)
    elif request.method == 'POST':
        if request.POST.get('posttype') == 'name':
            fuser.name = request.POST.get('name')
        if request.POST.get('posttype') == 'avatar':
            file = request.FILES['avatar']
            fs = FileSystemStorage()
            avatar = fs.save(file.name, file)
            fuser.avatar = avatar
        fuser.save()
        return redirect('user')


def user_post(request):
    template_name = "user_post.html"
    if request.user.is_anonymous:
        return redirect('/accounts/login/')
    if request.method == 'GET':
        fuser = FUser.objects.get(email=request.user)
        post = Post.objects.all().filter(author=fuser)
        get_filter = PostFilter(request.GET, post)
        if request.GET:
            if request.GET.get('title'):
                filter = request.GET.get('title')
                post = post.filter(title__icontains=filter)
            if request.GET.get('category'):
                filter = request.GET.getlist('category')
                post = post.filter(category__in=filter)
            if request.GET.get('added_after'):
                filter = request.GET.get('added_after')
                post = post.filter(data__gt=filter)
        paginator = Paginator(post.order_by('-data'), 3)
        page_number = request.GET.get('page')
        post = paginator.get_page(page_number)
        context = {
            'user': fuser,
            'user_post': post,
            'get_filter': get_filter,
        }
        return render(request, template_name, context)
    elif request.method == 'POST':
        Post.objects.get(id=request.POST.get('post')).delete()


def user_response(request):
    template_name = "user_response.html"
    if request.user.is_anonymous:
        return redirect('/accounts/login/')
    if request.method == 'GET':
        fuser = FUser.objects.get(email=request.user)
        post = Post.objects.all().filter(author=fuser)
        new_response = Response.objects.all().filter(post__in=post, new=False, accept=False)
        response = Response.objects.all().filter(post__in=post, new=True, accept=False)
        get_filter = ResponseFilter(request.GET, response)
        if request.GET:
            if request.GET.get('author'):
                filter = request.GET.get('author')
                response = response.filter(author__name__icontains=filter)
            if request.GET.get('post'):
                filter = request.GET.get('post')
                response = response.filter(post__title__icontains=filter)
            if request.GET.get('added_after'):
                filter = request.GET.get('added_after')
                response = response.filter(data__gt=filter)

        response = Paginator(response.order_by('-data'), 3).get_page(request.GET.get('page'))
        for i in new_response:
            i.new = True
            i.save()
        context = {
            'user': fuser,
            'new_response': new_response,
            'response': response,
            'get_filter': get_filter,
        }
        return render(request, template_name, context)
    elif request.method == 'POST':
        if request.POST.get('posttype') == 'accept':
            response = Response.objects.get(id=request.POST.get('post'))
            response.accept = True
            response.save()
            Response.accept_response(response)

            return redirect('user_response')
        if request.POST.get('posttype') == 'delete':
            Response.objects.get(id=request.POST.get('post')).delete()
            return redirect('user_response')
