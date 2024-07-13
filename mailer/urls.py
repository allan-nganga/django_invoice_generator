from django.urls import path
from .views import send_welcome_email

urlpatterns = [
    # path('invoice/<uuid:invoice_id>/send_mail/', send_email_view, name= 'send_email_view'),
    # path('invoice/<uuid:invoice_id>/send-welcome-email/', send_welcome_email, name='send_welcome_email'),
    path('send-welcome-email/', send_welcome_email, name='send_welcome_email'),
]