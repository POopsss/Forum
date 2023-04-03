from django.shortcuts import render
from django.views.generic import ListView, DetailView

from forum.models import *

class PostList(DetailView):
    model = Post
    ordering = '-data'
    template_name = 'main.html'
    context_object_name = 'post'

class FUserList(DetailView):
    model = FUser
    template_name = 'test.html'
    context_object_name = 'user'
