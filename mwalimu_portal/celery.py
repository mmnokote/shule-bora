import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mwalimu_portal.settings')

app = Celery('mwalimu_portal')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Ensure Celery retries broker connection on startup
app.conf.broker_connection_retry_on_startup = True

app.autodiscover_tasks()
