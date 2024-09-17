from datetime import timedelta
from django.utils import timezone
from invoicing_app.models import Invoice

def get_weekly_invoices():
    today = timezone.now().date()
    start_week = today - timedelta(days=today.weekday()) # Start of the week (Monday)
    end_week = start_week + timedelta(days=6) # End of the week(Sunday)
    return Invoice.objects.filter(created_at__date__range=[start_week, end_week])

def get_monthly_invoices():
    today = timezone.now().date()
    start_month = today.replace(day=1)  # Start of the month
    next_month = (start_month + timedelta(days=32)).replace(day=1)  # First day of the next month
    return Invoice.objects.filter(created_at__date__range=[start_month, next_month])

def get_yearly_invoices():
    today = timezone.now().date()
    start_year = today.replace(month=1, day=1)  # Start of the year
    next_year = start_year.replace(year=start_year.year + 1)  # Start of the next year
    return Invoice.objects.filter(created_at__date__range=[start_year, next_year])

def get_total_invoices_cost(invoices):
    total_cost = 0
    for invoice in invoices:
        total_cost += invoice.total_cost
    return total_cost