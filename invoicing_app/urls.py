from django.urls import path
from .views import generate_invoice_pdf, edit_invoice, delete_invoice, view_invoice, mark_as_paid, mark_as_unpaid, create_invoice, dashboard, invoice_list, invoice_detail, add_client, edit_client, delete_client, edit_settings,active_clients_list,client_list, mark_client_active, mark_client_inactive, overdue_invoices, due_invoices, inactive_clients_list

app_name = 'invoice_generator'

urlpatterns = [
    path('invoice/create/', create_invoice, name='create_invoice'),
    path('invoices/', invoice_list, name='invoice_list'),
    path('dashboard/', dashboard, name='dashboard'),
    path('invoice/<uuid:invoice_id>/details/', invoice_detail, name='invoice_detail'),
    path('invoice/<uuid:invoice_id>/pdf/', generate_invoice_pdf, name='generate_invoice_pdf'),
    path('invoice/<uuid:invoice_id>/view/', view_invoice, name='view_invoice'),
    path('invoice/<uuid:invoice_id>/edit/', edit_invoice, name='edit_invoice'),
    path('invoice/<uuid:invoice_id>/delete/', delete_invoice, name='delete_invoice'),
    path('invoice/<uuid:invoice_id>/mark_as_paid/', mark_as_paid, name='mark_as_paid'),
    path('invoice/<uuid:invoice_id>/mark_as_unpaid/', mark_as_unpaid, name='mark_as_unpaid'),
    path('client/add/', add_client, name='add_client'),
    path('client/<uuid:client_id>/edit/', edit_client, name='edit_client'),
    path('client/<uuid:client_id>/delete/', delete_client, name='delete_client'),
    path('settings/', edit_settings, name='settings'),
    path('clients/active/', active_clients_list, name='active_clients_list'),
    path('clients/inactive', inactive_clients_list, name='inactive_clients_list'),
    path('clients/all', client_list, name='client_list'),
    path('client/<uuid:client_uuid>/activate/', mark_client_active, name='mark_client_active'),
    path('client/<uuid:client_uuid>/deactivate/', mark_client_inactive, name='mark_client_inactive'),
    path('invoices/due/', due_invoices, name='due_invoices'),
    path('invoices/overdue/', overdue_invoices, name='overdue_invoices')
    # path('settings/edit', settings, name='settings'),
]