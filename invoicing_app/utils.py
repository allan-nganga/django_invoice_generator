from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from .models import Invoice

def generate_pdf(invoice, request=None):
    items = invoice.items.all()
    context = {
        'invoice': invoice,
        'items': items,
    }
    html_string = render_to_string('invoice/invoice_template.html', context)
    if request:
        html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    else:
        html = HTML(string=html_string)
    pdf = html.write_pdf()
    return pdf