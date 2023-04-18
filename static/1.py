from forum.models import *
from allauth.socialaccount.models import SocialApp

c = [
    'Танки',
    'Хилы',
    'ДД',
    'Торговцы',
    'Гилдмастеры',
    'Квестгиверы',
    'Кузнецы',
    'Кожевники',
    'Зельевары',
    'Мастера заклинаний',
]

for i in c:
    Category(category=i).save()

provider = 'google'
name = 'Google'
client_id = '630972283500-2sseoi461lk3dm1n19lvscb568i3vh40.apps.googleusercontent.com'
secret = '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'

SocialApp(provider=provider, name=name,client_id=client_id, secret=secret).save()

provider = 'yandex'
name = 'Yandex'
client_id = '9e73c001fdac4203bbeb44f5daa810fb'
secret = 'f6d36c8af5da472e8e758af816a02bd1'

SocialApp(provider=provider, name=name,client_id=client_id, secret=secret).save()
