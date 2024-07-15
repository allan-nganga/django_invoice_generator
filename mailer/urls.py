from django.urls import path
from .views import send_invoice_reminder

urlpatterns = [
    # path('invoice/<uuid:invoice_id>/send_mail/', send_email_view, name= 'send_email_view'),
    # path('invoice/<uuid:invoice_id>/send-welcome-email/', send_welcome_email, name='send_welcome_email'),
    path('invoice/<uuid:invoice_id>/send_email', send_invoice_reminder, name='send_invoice_reminder'),
]