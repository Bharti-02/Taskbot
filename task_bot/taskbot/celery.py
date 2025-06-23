import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskbot.settings')

app = Celery('taskbot')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
