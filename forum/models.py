from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from froala_editor.fields import FroalaField
from .tasks import mail_sender


class FUser(models.Model):
    name = models.CharField(max_length=32)
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='', blank=True)

    def new_user(self):
        mail = {
            'to': [self.email.email],
            'subject': 'Добро пожаловать на 127.0.0.1:8000!',
            'text': f'Добро пожаловать на 127.0.0.1:8000!',
            'html': f'Добро пожаловать на <a href="http://127.0.0.1:8000/">сайт</a>!',
        }
        mail_sender.delay(mail)
        # mail_sender(mail)

    def __str__(self):
        return f'{self.name}: {self.email.email}'


class Post(models.Model):
    author = models.ForeignKey('FUser', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=128)
    text = FroalaField(theme='dark')
    category = models.ManyToManyField('Category', through='PostCategory')

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.author.name}: {self.title}'


class Response(models.Model):
    author = models.ForeignKey('FUser', on_delete=models.CASCADE, unique=False)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, unique=False)
    date = models.DateTimeField(auto_now_add=True)
    text = RichTextField(config_name='default')
    new = models.BooleanField(default=True)
    accept = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def new_response(self):
        mail = {
            'to': [self.author.email.email],
            'subject': 'Вам пришёл отклик на объявление',
            'text': f'{self.author.name}, оставил отклик на ваше объявление: {self.text}',
            'html': f'<b>{self.author.name}</b>, оставил отклик:<br>{self.text}на ваше объявление:<br>{self.post.title}',
        }
        mail_sender.delay(mail)
        # mail_sender(mail)

    def accept_response(self):
        mail = {
            'to': [self.author.email.email],
            'subject': 'Ваш отклик был принят!',
            'text': f'{self.author.name}, ваш отклик был принят!',
            'html': (
                f'<b>{self.author.name}</b>, ваш отклик:<br>{self.text} на статью:<br>{self.post.title}<br><b>был принят!</b>'
            ),
        }
        mail_sender.delay(mail)
        # mail_sender(mail)

    def __str__(self):
        return f'{self.author} {self.date}'


class Category(models.Model):
    category = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category.title()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, unique=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, unique=False)

    class Meta:
        unique_together = ('post', 'category',)
