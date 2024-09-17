from django.shortcuts import render
from .utils import get_weekly_invoices, get_monthly_invoices, get_yearly_invoices

# Create your views here.
def weekly_invoice_report(request):
    invoices = get_weekly_invoices()
    total_cost = get_total_invoices_cost(invoices)
    return render(request, 'reports/weekly_invoice_report.html', {'invoices': invoices})

def monthly_invoice_report(request):
    invoices = get_monthly_invoices()
    total_cost = get_total_invoices_cost(invoices)
    return render(request, 'reports/monthly_invoice_report.html', {'invoices': invoices})

def yearly_invoice_report(request):
    invoices = get_yearly_invoices()
    total_cost = get_total_invoices_cost(invoices)
    return render(request, 'reports/yearly_invoice_report.html', {'invoices': invoices})