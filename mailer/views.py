from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from invoicing_app.utils import generate_pdf
from invoicing_app.models import Invoice

def send_invoice_reminder(request, invoice_id):
    invoice = get_object_or_404(Invoice, invoice_id=invoice_id)
    client_email = invoice.client.client_email
    client_name = invoice.client.client_name
    due_date = invoice.due_date
    
    # Render email content
    email_content = render_to_string('mailer/reminder.html', {
        'client_name': client_name,
        'invoice_id': invoice.invoice_id,
        'due_date': due_date
    })
    
    # Generate PDF invoice
    pdf_file = generate_pdf(invoice)
    
    # Create email
    email = EmailMessage(
        subject='Invoice Reminder',
        body=email_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[client_email]
    )
    
    # Attach PDF
    email.attach(f'invoice_{invoice.invoice_id}.pdf', pdf_file, 'application/pdf')
    
    # Send email
    email.send()

    return HttpResponse('Reminder sent successfully.')