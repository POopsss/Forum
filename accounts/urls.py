from django.urls import path
from .views import user, user_post, user_reply, accept_reply

urlpatterns = [
    path('', user, name='user'),
    path('post/', user_post, name='user_post'),
    path('reply/', user_reply, name='user_reply'),
    path('accept_reply/', accept_reply, name='accept_reply'),
]
