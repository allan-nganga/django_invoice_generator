from django.shortcuts import render
from django.core.mail import EmailMessage
from invoicing_app.views import generate_invoice_pdf

def send_email_with_pdf(to_email):
    subject = 'Subject'
    body = 'Hi. Please find attached invoice.'
    from_email = 'allen.nganga0@gmail.com'

    email = EmailMessage(subject, body, from_email, [to_email])

    pdf = generate_invoice_pdf()
    email.attach('document.pdf', pdf.read(), 'application/pdf')

    email.send()