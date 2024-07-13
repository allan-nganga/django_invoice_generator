# email_utils.py
from django.core.mail import EmailMessage

def send_invoice_email(to_email, pdf):
    email = EmailMessage(subject, body, 'allen.nganga0@gmail.com', [to_email])
    email.attach('invoice.pdf', pdf.read(), 'application/pdf')
    email.send()