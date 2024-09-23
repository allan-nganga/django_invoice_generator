from datetime import timedelta
from django.utils import timezone
from invoicing_app.models import Invoice

def filter_invoices_by_date_range(start_date, end_date):
    """
    Returns invoices filtered by a custom date range.
    """
    return Invoice.objects.filter(created_at__date__range=[start_date, end_date])

def get_weekly_invoices():
    today = timezone.now().date()
    start_week = today - timedelta(days=today.weekday())
    end_week = start_week + timedelta(days=6)
    return filter_invoices_by_date_range(start_week, end_week)

def get_monthly_invoices():
    today = timezone.now().date()
    start_month = today.replace(day=1)
    next_month = (start_month + timedelta(days=32)).replace(day=1)
    return filter_invoices_by_date_range(start_month, next_month)

def get_yearly_invoices():
    today = timezone.now().date()
    start_year = today.replace(month=1, day=1)
    next_year = start_year.replace(year=start_year.year + 1)
    return filter_invoices_by_date_range(start_year, next_year)