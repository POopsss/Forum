from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from forum.models import FUser, Post, Response
from .forms import UserForm
from django.core.paginator import Paginator


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
        paginator = Paginator(Post.objects.all().filter(author=fuser).order_by('id'), 3)
        page_number = request.GET.get('page')
        post = paginator.get_page(page_number)
        context = {
            'user': fuser,
            'user_post': post,
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
        new_response = []
        response = []
        for post in post:
            new_response += Response.objects.all().filter(post=post, new=False, accept=False)
            response += Response.objects.all().filter(post=post, new=True, accept=False)
        paginator = Paginator(response, 3)
        page_number = request.GET.get('page')
        response = paginator.get_page(page_number)
        for i in new_response:
            i.new = True
            i.save()
        context = {
            'user': fuser,
            'new_response': new_response,
            'response': response,
        }
        return render(request, template_name, context)
    elif request.method == 'POST':
        if request.POST.get('posttype') == 'accept':
            response = Response.objects.get(id=request.POST.get('post'))
            response.accept = True
            response.save()
            return redirect('user_response')
        if request.POST.get('posttype') == 'delete':
            Response.objects.get(id=request.POST.get('post')).delete()
            return redirect('user_response')
