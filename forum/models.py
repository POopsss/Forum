from django.db import models
from django.contrib.auth.models import User


class FUser(models.Model):
    name = models.CharField(max_length=32)
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    userpost = models.ForeignKey('Post', on_delete=models.CASCADE)
    usercomment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    # like = models.ForeignKey()


class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    author = models.ForeignKey(FUser, on_delete=models.CASCADE)
    # rating = models.ForeignKey(FUser, through='Postrating')


class Comment(models.Model):
    author = models.OneToOneField(FUser, on_delete=models.CASCADE)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    text = models.TextField()


class Like(models.Model):
