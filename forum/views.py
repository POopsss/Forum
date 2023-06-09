from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from forum.models import *
from forum.forms import ReplyForm, PostForm
from .filters import PostFilter


class PostList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'main.html'
    context_object_name = 'list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context



class PostDetail(DetailView):
    model = Post
    ordering = '-date'
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reply'] = ReplyForm
        return context

    def post(self, request, *args, **kwargs):
        user = FUser.objects.get(email_id=request.user.id)
        post = Post.objects.get(id=kwargs.get('pk'))

        if request.POST.get('posttype') == 'reply':
            text = request.POST.get('text')
            form = ReplyForm({'author': user, 'post': post, 'text': text})
            if form.is_valid():
                form.save()

        return redirect('post_detail', pk=kwargs.get('pk'))


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'

    def get(self, request, *args, **kwargs):
        context = super().get(self, request, *args, **kwargs)
        if request.user.is_anonymous:
            return redirect('main')
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = FUser.objects.get(email=self.request.user)
        return super().form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_update.html'

    def get(self, request, *args, **kwargs):
        context = super().get(self, request, *args, **kwargs)
        if self.object.author.email == request.user:
            return context
        return redirect('main')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = FUser.objects.get(email=self.request.user)
        return super().form_valid(form)


class AuthorDetail(DetailView):
    model = FUser
    template_name = 'author.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.all().filter(author=kwargs.get('object'))
        return context


