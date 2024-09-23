from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('reports/invoices/', views.invoice_report_view, name='invoice_report_view'),
]