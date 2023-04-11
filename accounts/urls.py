from django.urls import path
from .views import user

urlpatterns = [
    path('user/', user, name='user'),
    # path('user/', User.as_view(), name='user'),
    # path('user/update/', UserUpdate.as_view(), name='userupdate'),
]