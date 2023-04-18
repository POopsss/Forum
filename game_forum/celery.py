import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_forum.settings')

app = Celery('game_forum')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
