"""Celery application for background tasks."""

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example.settings')

app = Celery('devind')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks([app for app in settings.INSTALLED_APPS])

if __name__ == '__main__':
    app.start()
