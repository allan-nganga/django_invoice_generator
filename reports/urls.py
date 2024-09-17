from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('reports/invoices/weekly/', views.weekly_invoice_report, name='weekly_invoice_report'),
    path('reports/invoices/monthly/', views.monthly_invoice_report, name='monthly_invoice_report'),
    path('reports/invoices/yearly/', views.yearly_invoice_report, name='yearly_invoice_report'),
]