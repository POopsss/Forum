from django.urls import path
from .views import user, user_post, user_response

urlpatterns = [
    path('user/', user, name='user'),
    path('user/post/', user_post, name='user_post'),
    path('user/response/', user_response, name='user_response'),
]
