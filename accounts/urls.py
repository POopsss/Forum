from django.urls import path
from .views import user, user_post

urlpatterns = [
    path('user/', user, name='user'),
    path('user/post/', user_post, name='user_post'),
]
