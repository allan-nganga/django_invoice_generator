from django.urls import path
from .views import generate_invoice_pdf, edit_invoice, delete_invoice, view_invoice, mark_as_paid, mark_as_unpaid, create_invoice, home, invoice_list, invoice_detail

app_name = 'invoice_generator'

urlpatterns = [
    path('create/', create_invoice, name='create_invoice'),
    path('invoices/', invoice_list, name='invoice_list'),
    path('home/', home, name='home'),
    path('invoice/<int:invoice_id>/', invoice_detail, name='invoice_detail'),
    path('invoice/<int:invoice_id>/pdf/', generate_invoice_pdf, name='generate_invoice_pdf'),
    path('invoice/<int:invoice_id>/', view_invoice, name='view_invoice'),
    path('invoice/<int:invoice_id>/edit/', edit_invoice, name='edit_invoice'),
    path('invoice/<int:invoice_id>/delete/', delete_invoice, name='delete_invoice'),
    path('invoice/<int:invoice_id>/mark_as_paid/', mark_as_paid, name='mark_as_paid'),
    path('invoice/<int:invoice_id>/mark_as_unpaid/', mark_as_unpaid, name='mark_as_unpaid'),
]