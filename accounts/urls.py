from django.urls import path
from .views import user, user_post, user_response

urlpatterns = [
    path('', user, name='user'),
    path('post/', user_post, name='user_post'),
    path('response/', user_response, name='user_response'),
]
