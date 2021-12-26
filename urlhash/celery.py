import os

from celery import Celery
from django.db.models import Q
from datetime import date
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urlhash.settings')
app = Celery('urlhash')
app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(name='delete_expired')
def delete_expired():
    from short.models import Urls
    expired = Urls.objects.filter(~Q(exhausted__in=[True]) | ~Q(expires_on__lt=date.today()))
    expired.delete()

app.conf.beat_schedule = {
    'delete-expired-links': {
        'task': 'delete_expired',
        'schedule': timedelta(seconds=5),
    },
}