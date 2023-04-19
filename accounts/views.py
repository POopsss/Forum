from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from forum.models import FUser, Post, Reply
from .forms import UserForm
from django.core.paginator import Paginator
from forum.filters import PostFilter, ReplyFilter


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
                post = post.filter(date__gt=filter)
        paginator = Paginator(post.order_by('-date'), 10)
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
        return redirect('user_post')


def user_reply(request):
    template_name = "user_reply.html"
    if request.user.is_anonymous:
        return redirect('/accounts/login/')
    if request.method == 'GET':
        fuser = FUser.objects.get(email=request.user)
        post = Post.objects.all().filter(author=fuser)
        new_reply = Reply.objects.all().filter(post__in=post, new=False, accept=False)
        reply = Reply.objects.all().filter(post__in=post, new=True, accept=False)

        get_filter = ReplyFilter(request.GET, reply)
        if request.GET:
            if request.GET.get('author'):
                filter = request.GET.get('author')
                reply = reply.filter(author__name__icontains=filter)
            if request.GET.get('post'):
                filter = request.GET.get('post')
                reply = reply.filter(post__title__icontains=filter)
            if request.GET.get('added_after'):
                filter = request.GET.get('added_after')
                reply = reply.filter(date__gt=filter)

        reply = Paginator(reply.order_by('-date'), 10).get_page(request.GET.get('page'))
        for i in new_reply:
            i.new = True
            i.save()
        context = {
            'user': fuser,
            'new_reply': new_reply,
            'reply': reply,
            'get_filter': get_filter,
        }
        return render(request, template_name, context)
    elif request.method == 'POST':
        if request.POST.get('posttype') == 'accept':
            reply = Reply.objects.get(id=request.POST.get('post'))
            reply.accept = True
            reply.save()
            Reply.accept_reply(reply)

            return redirect('user_reply')
        if request.POST.get('posttype') == 'delete':
            Reply.objects.get(id=request.POST.get('post')).delete()
            return redirect('user_reply')


def accept_reply(request):
    template_name = "accept_reply.html"
    if request.user.is_anonymous:
        return redirect('/accounts/login/')
    if request.method == 'GET':
        fuser = FUser.objects.get(email=request.user)
        post = Post.objects.all().filter(author=fuser)
        reply = Reply.objects.all().filter(post__in=post, accept=True)

        get_filter = ReplyFilter(request.GET, reply)
        if request.GET.get('author'):
            filter = request.GET.get('author')
            reply = reply.filter(author__name__icontains=filter)
        if request.GET.get('post'):
            filter = request.GET.get('post')
            reply = reply.filter(post__title__icontains=filter)
        if request.GET.get('added_after'):
            filter = request.GET.get('added_after')
            reply = reply.filter(date__gt=filter)

        reply = Paginator(reply.order_by('-date'), 10).get_page(request.GET.get('page'))
        context = {
            'user': fuser,
            'reply': reply,
            'get_filter': get_filter,
        }
        return render(request, template_name, context)
    elif request.method == 'POST':
        if request.POST.get('posttype') == 'delete':
            Reply.objects.get(id=request.POST.get('post')).delete()
            return redirect('accept_reply')
