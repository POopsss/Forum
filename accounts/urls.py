from django.urls import path
from .views import user

urlpatterns = [
    path('user/', user, name='user'),
]