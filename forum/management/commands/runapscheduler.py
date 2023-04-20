import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django_apscheduler import util
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from custom_sign.models import EmailVerified
from datetime import datetime, timezone, timedelta
from forum.models import FUser
from allauth.account.models import EmailAddress

logger = logging.getLogger(__name__)


def my_job():
    verified = EmailVerified.objects.all()
    print('start my_job')
    for i in verified:
        delta = datetime.now().date() - i.date.date()
        if delta.days >= 1:
            email = i.email
            user = User.objects.get(email=email)
            fuser = FUser.objects.get(email=user)
            eaddres = EmailAddress.objects.get(user=user)
            i.delete()
            user.delete()
            fuser.delete()
            eaddres.delete()


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(minute="11", hour="11"),
            id="my_job",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: 'delete_old_job_executions'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")