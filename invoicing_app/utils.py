from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML, CSS
from .models import Invoice
from django.conf import settings
import os

def generate_pdf(invoice, request=None):
    items = invoice.items.all()
    context = {
        'invoice': invoice,
        'items': items,
    }
    html_string = render_to_string('invoice/invoice_template.html', context)

    if request:
        css_url = request.build_absolute_uri(settings.STATIC_URL + 'invoice/invoice_template.css')
        html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    else:
        css_path = os.path.join(settings.STATIC_ROOT, 'invoice/invoice_template.css')
        css_url = 'file://' + css_path
        html = HTML(string=html_string)

    pdf = html.write_pdf(stylesheets=[CSS(css_url)])
    return pdf