from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'invoice_generator.settings')

app = Celery('invoice_generator')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'generate-invoices-every-minute': {
        'task': 'mailer.tasks.generate_invoice_task',
        'schedule': crontab(minute='*'),  # Executes every minute
        'args': (1, 'minute'),  # Add the appropriate client_id
    },
    'generate-invoices-hourly': {
        'task': 'mailer.tasks.generate_invoice_task',
        'schedule': crontab(minute=0, hour='*'),  # Executes every hour
        'args': (1, 'hourly'),  # Add the appropriate client_id
    },
    'generate-invoices-daily': {
        'task': 'mailer.tasks.generate_invoice_task',
        'schedule': crontab(hour=0, minute=0),  # Executes daily at midnight
        'args': (1, 'daily'),  # Add the appropriate client_id
    },
    'generate-invoices-weekly': {
        'task': 'mailer.tasks.generate_invoice_task',
        'schedule': crontab(hour=0, minute=0, day_of_week='monday'),  # Executes every Monday at midnight
        'args': (1, 'weekly'),  # Add the appropriate client_id
    },
    'generate-invoices-monthly': {
        'task': 'mailer.tasks.generate_invoice_task',
        'schedule': crontab(hour=0, minute=0, day_of_month='1'),  # Executes on the first day of the month
        'args': (1, 'monthly'),  # Add the appropriate client_id
    },
    'generate-invoices-yearly': {
        'task': 'mailer.tasks.generate_invoice_task',
        'schedule': crontab(hour=0, minute=0, day_of_month='1', month_of_year='1'),  # Executes on the first day of the year
        'args': (1, 'yearly'),  # Add the appropriate client_id
    },
}
