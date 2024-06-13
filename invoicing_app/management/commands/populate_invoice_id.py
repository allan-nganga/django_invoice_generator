import string
import random
from django.core.management.base import BaseCommand
from django.db.models import Count
from invoicing_app.models import Invoice

def generate_unique_invoice_id():
    while True:
        invoice_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        if not Invoice.objects.filter(invoice_id=invoice_id).exists():
            return invoice_id

class Command(BaseCommand):
    help = 'Populate invoice_id with unique values for existing invoices'

    def handle(self, *args, **kwargs):
        invoices = Invoice.objects.filter(invoice_id__isnull=True)
        for invoice in invoices:
            invoice.invoice_id = generate_unique_invoice_id()
            invoice.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully updated invoice_id for Invoice {invoice.id}'))

        # Check for duplicates and handle them
        duplicates = Invoice.objects.values('invoice_id').annotate(id_count=Count('id')).filter(id_count__gt=1)
        for item in duplicates:
            duplicate_invoices = Invoice.objects.filter(invoice_id=item['invoice_id'])
            for i, invoice in enumerate(duplicate_invoices):
                if i == 0:
                    continue
                invoice.invoice_id = generate_unique_invoice_id()
                invoice.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully updated duplicate invoice_id for Invoice {invoice.id}'))