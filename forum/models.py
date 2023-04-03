from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


class FUser(models.Model):
    name = models.CharField(max_length=32)
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('FUser', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=128)
    text = CKEditor5Field(verbose_name='Содержание', config_name='extends')
    category = models.ManyToManyField('Category', through='PostCategory')
    rating = models.FloatField(default=0)

    def setrating(self):
        self.rating = 0
        for i in PostRating.objects.all().filter(post_id=self.id):
            self.rating += i.rating
        self.rating = self.rating / len(PostRating.objects.all().filter(post_id=self.id))
        self.save()

    # def __str__(self):
    #     return f'{self.title}: {self.text}'


class Comment(models.Model):
    author = models.ForeignKey('FUser', on_delete=models.CASCADE, unique=False)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, unique=False)
    data = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    like = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.text}'

    def setlike(self):
        self.like = len(CommentLike.objects.all().filter(comment_id=self.id))
        self.save()


# class PostComment(models.Model):
#     post = models.ForeignKey('Post', on_delete=models.CASCADE, unique=False)
#     comment = models.ForeignKey('Comment', on_delete=models.CASCADE, unique=False)


class PostRating(models.Model):
    user = models.ForeignKey('FUser', on_delete=models.CASCADE, unique=False)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, unique=False)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        unique_together = ('user', 'post',)

    def __str__(self):
        return f'{self.user} {self.post} {self.rating}'


class CommentLike(models.Model):
    user = models.ForeignKey('FUser', on_delete=models.CASCADE, unique=False)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, unique=False)

    class Meta:
        unique_together = ('user', 'comment',)

    def __str__(self):
        return f'{self.user} {self.comment}'


class Category(models.Model):
    category = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category.title()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, unique=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, unique=False)

    class Meta:
        unique_together = ('post', 'category',)
