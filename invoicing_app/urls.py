from django.urls import path
from .views import generate_invoice_pdf, edit_invoice, delete_invoice, view_invoice, mark_as_paid, mark_as_unpaid, create_invoice, dashboard, invoice_list, invoice_detail, add_client, edit_client, delete_client, edit_settings,active_clients_list,client_list, mark_client_active, mark_client_inactive

app_name = 'invoice_generator'

urlpatterns = [
    path('invoice/create/', create_invoice, name='create_invoice'),
    path('invoices/', invoice_list, name='invoice_list'),
    path('dashboard/', dashboard, name='dashboard'),
    path('invoice/<int:invoice_id>/details', invoice_detail, name='invoice_detail'),
    path('invoice/<int:invoice_id>/pdf/', generate_invoice_pdf, name='generate_invoice_pdf'),
    path('invoice/<uuid:id>/view', view_invoice, name='view_invoice'),
    path('invoice/<int:invoice_id>/edit/', edit_invoice, name='edit_invoice'),
    path('invoice/<int:invoice_id>/delete/', delete_invoice, name='delete_invoice'),
    path('invoice/<int:invoice_id>/mark_as_paid/', mark_as_paid, name='mark_as_paid'),
    path('invoice/<int:invoice_id>/mark_as_unpaid/', mark_as_unpaid, name='mark_as_unpaid'),
    path('client/add/', add_client, name='add_client'),
    path('client/edit/<uuid:client_id>/', edit_client, name='edit_client'),
    path('client/delete/<uuid:client_id>/', delete_client, name='delete_client'),
    path('settings/', edit_settings, name='settings'),
    path('client/active/', active_clients_list, name='active_clients_list'),
    path('clients/', client_list, name='client_list'),
    path('client/<int:client_id>/activate/', mark_client_active, name='mark_client_active'),
    path('client/<int:client_id>/deactivate/', mark_client_inactive, name='mark_client_inactive'),
    # path('settings/edit', settings, name='settings'),
]