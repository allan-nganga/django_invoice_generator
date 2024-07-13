"""
from django.shortcuts import render, get_object_or_404
from .email_utils import send_invoice_email
from django.http import HttpResponseRedirect
from invoicing_app.models import Invoice
from invoicing_app.views import generate_invoice_pdf
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def send_email_view(request):
    if request.method == 'POST':
        to_email = request.POST.get('email-address')
        subject = request.POST.get('subject')
        body = request.POST.get('email-body')
        
        # Assuming you have a function to generate the PDF and send the email
        pdf = generate_invoice_pdf(invoice)
        send_invoice_email(to_email, subject, body)

        return HttpResponseRedirect('{% url "invoicing_app:invoice_list" %}')  # Redirect to a success page or the same form with a success message

    return render(request, 'mailer/send_email.html', {'invoice': invoice})


from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse


def send_welcome_email(request):
    try:
        send_mail(
        'Welcome',
        'Here is the message.',
        'billing@creative-junk.com',
        ['allen.nganga7@gmail.com'],
        fail_silently=False,
    )
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    except Exception as e:
        return HttpResponse(f'An error occurred: {e}')
    return render(request, 'mailer/send_email.html')
"""

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmailForm

def send_welcome_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            try:
                send_mail(
                    subject,
                    body,
                    'billing@creative-junk.com',  # From email
                    [recipient],  # To email
                    fail_silently=False,
                )
                return HttpResponse('Email sent successfully.')
            except Exception as e:
                return HttpResponse(f'An error occurred: {e}')
    else:
        form = EmailForm()
    return render(request, 'mailer/send_email.html', {'form': form})
