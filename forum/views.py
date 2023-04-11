from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, FormView

from forum.models import *
from forum.forms import LikeForm, RatingForm, CommentForm, PostForm


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
        context['comment'] = CommentForm
        # context['postform'] = PostForm
        return context

    def post(self, request, *args, **kwargs):
        user = FUser.objects.get(email_id=request.user.id)
        post = Post.objects.get(id=kwargs.get('pk'))
        if request.POST.get('posttype') == 'commentlike':
            comment = Comment.objects.get(id=request.POST.get('commentid'))
            try:
                CommentLike.objects.get(user=user, comment=comment).delete()
                comment.setlike()
                return redirect('post_detail', pk=kwargs.get('pk'))
            except:
                form = LikeForm({'user': user, 'comment': comment})
                if form.is_valid():
                    form.save()
                    comment.setlike()

        if request.POST.get('posttype') == 'postrating':
            rating = int(request.POST.get('rating'))
            try:
                form = PostRating.objects.get(user=user, post=post)
                form.rating = rating
                form.save()
                post.setrating()
                return redirect('post_detail', pk=kwargs.get('pk'))
            except:
                form = RatingForm({'user': user, 'post': post, 'rating': rating})
                if form.is_valid():
                    form.save()
                    post.setrating()

        if request.POST.get('posttype') == 'comment':
            text = request.POST.get('text')
            form = CommentForm({'author': user, 'post': post, 'text': text, 'like': 0})
            if form.is_valid():
                form.save()

        return redirect('post_detail', pk=kwargs.get('pk'))


class CommentList(ListView):
    model = Comment
    # queryset = Comment.objects.filter(po)
    template_name = 'test.html'
    context_object_name = 'com'


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    # context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['create'] = PostForm
    #     return context
