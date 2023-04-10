from django.urls import path
from .views import User, red

urlpatterns = [
    path('user/', red),
    # path('user/', User.as_view(), name='user'),
]