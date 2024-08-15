from celery import shared_task
from .views import automate_invoicing

@shared_task
def generate_invoice_task(client_id, frequency):
    automate_invoicing(client_id, frequency)