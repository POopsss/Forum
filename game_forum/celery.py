import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_forum.settings')

app = Celery('game_forum')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'mail_every_monday': {
        'task': 'forum.tasks.weekly_news',
        'schedule': crontab(hour=7, minute=3, day_of_week='friday'),
    },
}