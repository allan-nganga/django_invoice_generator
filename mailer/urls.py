from django.urls import path
from .views import send_invoice_reminder

urlpatterns = [
    path('invoice/<uuid:invoice_id>/send_email', send_invoice_reminder, name='send_invoice_reminder'),
]