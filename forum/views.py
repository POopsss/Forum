from django.shortcuts import render
from django.views.generic import ListView

from forum.models import *

class PostList(ListView):
    model = Post
    ordering = '-data'
    template_name = 'main.html'
    context_object_name = 'post'
