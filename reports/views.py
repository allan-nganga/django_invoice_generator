from django.shortcuts import render
from django.utils import timezone
from invoicing_app.models import Invoice, Client, Settings
from .utils import get_weekly_invoices, get_monthly_invoices, get_yearly_invoices, filter_invoices_by_date_range

# Create your views here.
def invoice_report_view(request):
    invoices = Invoice.objects.all() # Start with all invoices

    # Get filter data from the form
    date_filter = request.GET.get('date_filter')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    payment_status = request.GET.get('payment_status')
    # client_name = request.GET.get('client')
    # company_id = request.GET.get('company')

    # Filter by date
    if date_filter == 'weekly':
        invoices = get_weekly_invoices()
    elif date_filter == 'monthly':
        invoices = get_monthly_invoices()
    elif date_filter == 'yearly':
        invoices = get_yearly_invoices()
    elif date_filter == 'custom' and start_date and end_date:
        invoices = filter_invoices_by_date_range(start_date, end_date)

    # Filter by payment status
    if payment_status == 'paid':
        invoices = invoices.filter(paid=True)
    elif payment_status == 'unpaid':
        invoices = invoices.filter(paid=False)

    """
    # Filter by client
    if client_name:
        invoices = invoices.filter(client__client_name=client_name)

    # Filter by company
    if company_id:
        invoices = invoices.filter(created_by__settings__company_id=company_id)

    # Get all clients and companies for the filter form
    clients = Client.objects.all()
    companies = Settings.objects.all()
    """

    # Calculate total amounts for paid and unpaid invoices
    paid_invoices = invoices.filter(paid=True)
    unpaid_invoices = invoices.filter(paid=False)

    total_paid_amount = sum(invoice.total_cost for invoice in paid_invoices)
    total_unpaid_amount = sum(invoice.total_cost for invoice in unpaid_invoices)


    return render(request, 'reports/invoice_reports.html', {
        'invoices':invoices,
        'total_paid_amount': total_paid_amount,
        'total_unpaid_amount': total_unpaid_amount
    })