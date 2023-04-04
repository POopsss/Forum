from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from forum.models import *
from forum.forms import LikeForm, RatingForm


class PostList(ListView):
    model = Post
    ordering = '-data'
    template_name = 'test2.html'
    context_object_name = 'list'


class PostDetail(DetailView):
    model = Post
    ordering = '-data'
    template_name = 'main.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = Comment.objects.filter(post_id=self.object.id)
        context['like'] = LikeForm
        context['rating'] = RatingForm
        # print('----------------------')
        # print(LikeForm)
        # print('----------------------')
        return context

    def post(self, request, *args, **kwargs):
        user = FUser.objects.get(email_id=request.user.id)
        if request.POST.get('posttype') == 'commentlike':
            form = LikeForm({'user': user, 'comment': request.POST.get('commentid')})
            if form.is_valid():
                form.save()
        # print(type(request.content))
        # print('---------------------------------')
        # LikeForm({'user': FUser.objects.get(email_id=request.user.id), 'comment': request.POST.get('commentid')}).save()
        return redirect('post_detail', pk=kwargs.get('pk'))


class CommentList(ListView):
    model = Comment
    # queryset = Comment.objects.filter(po)
    template_name = 'test.html'
    context_object_name = 'com'



class FUserList(DetailView):
    model = FUser
    template_name = 'test.html'
    context_object_name = 'user'
