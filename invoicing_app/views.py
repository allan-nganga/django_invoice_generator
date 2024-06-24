from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from .models import Invoice, Client, Settings, InvoiceItem
from .forms import InvoiceForm, InvoiceItemForm, ClientForm, SettingsForm
from weasyprint import HTML
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F, FloatField, ExpressionWrapper
from django.contrib import messages
from django.contrib.auth.models import User
from django_countries import countries
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

# View invoice function
@login_required
def view_invoice(request,invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    return render(request, 'invoice/invoice_detail.html', {'invoice': invoice})

# Edit invoice function
@login_required
def edit_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    InvoiceItemFormSet = forms.inlineformset_factory(Invoice, InvoiceItem, form=InvoiceItemForm, extra=1)
    
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        formset = InvoiceItemFormSet(request.POST, instance= invoice)
        if form.is_valid() and formset.is_valid():
            form.save()
            return redirect('invoicing_app:invoice_detail', invoice_id=invoice.id)
    else:
        form = InvoiceForm(instance=invoice)
        formset = InvoiceItemFormSet(instance=invoice)

        context = {
            'form': form,
            'formset':formset,
            'invoice':invoice
        }
    return render(request, 'invoice/edit_invoice.html', context)

# Delete invoice function
@login_required
def delete_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if request.method == 'POST':
        invoice.delete()
        return redirect('invoicing_app:invoice_list')
    return render(request, 'invoice/delete_invoice.html', {'invoice': invoice})

# Generate PDF
@login_required
def generate_invoice_pdf(request, invoice_id):
    # Retrieve the invoice object
    invoice = get_object_or_404(Invoice, id=invoice_id)

    # Prepare context data for the template
    items = invoice.items.all()
    context = {
        'invoice': invoice,
        'items': items,
    }
    # Render the HTML template with invoice data
    # template = get_template('invoice/invoice_template.html')
    html_string = render_to_string('invoice/invoice_template.html', context)

    # Create a PDF file using WeasyPrint
    # pdf_file = weasyprint.HTML(string=html_string).write_pdf(stylesheets=[weasyprint.css('login/static/invoice/style.css')])
    html = HTML(string =html_string, base_url=request.build_absolute_uri('/'))
    pdf = html.write_pdf()

    # Create a HTTP response with PDF as content type
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.id}.pdf"'
    return response

# invoice create function
@login_required
def create_invoice(request):
    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)
        if invoice_form.is_valid():
            invoice = invoice_form.save(commit=False)
            invoice.created_by = request.user
            invoice.save()

            item_descriptions = request.POST.getlist('item_description')
            item_quantities = request.POST.getlist('item_quantity')
            item_prices = request.POST.getlist('item_price')

            for description, quantity, price in zip(item_descriptions, item_quantities, item_prices):
                item_form = InvoiceItemForm({
                    'description': description,
                    'quantity': quantity,
                    'price': price,
                    'invoice': invoice.id
                })
                if item_form.is_valid():
                    item = item_form.save(commit=False)
                    item.invoice = invoice
                    item.created_by = request.user
                    item.save()
            return redirect('invoicing_app:invoice_detail', invoice_id=invoice.id)
        else:
            return render(request, 'invoice/create_invoice.html', {'invoice_form': invoice_form})

    else:
        invoice_form = InvoiceForm()
    clients = Client.objects.filter(active_status=True)
    return render(request, 'invoice/create_invoice.html', {'invoice_form': invoice_form, 'clients':clients})

"""
@login_required
def create_invoice_item(request, invoice_id):
    invoice = Invoice.objects.get(invoice_id=invoice_id)
    if request.method == 'POST':
        item_form = InvoiceItemForm(request.POST)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.invoice = invoice
            item.save()
            return redirect('invoicing_app:invoice_detail', invoice_id=invoice.invoice_id)
    else:
        item_form = InvoiceItemForm(initial={'invoice': invoice})

    return render(request, 'invoice/create_invoice.html', {'item_form': item_form, 'invoice': invoice})
"""
     
# Fetch and display invoices
@login_required
def invoice_list(request):
    # context = {'page_title': 'Invoice List'}
    # invoice = Invoice.objects.all().order_by('-created_at')

    # Search-bar function
    query = request.GET.get('q')
    if query:
        invoices = Invoice.objects.filter(
            Q(id__icontains=query) |
            Q(client__client_name__icontains=query)
        ).order_by('-created_at')
    else:
        invoices = Invoice.objects.all().order_by('-created_at')

    paginator = Paginator(invoices, 9)
    page = request.GET.get('page')
    try:
        invoices = paginator.page(page)
    except PageNotAnInteger:
        invoices = paginator.page(1)
    except EmptyPage:
        invoices = paginator.page(paginator.num_pages)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('invoice/invoice_list_partial.html', {'invoices': invoices})
        data = {
            'html': html,
            'page_number': invoices.number,
            'has_previous': invoices.has_previous(),
            'has_next': invoices.has_next(),
            'num_pages': paginator.num_pages,
            'total_items': paginator.count,
        }
        return JsonResponse(data)
    
    return render(request, 'invoice/invoice_list.html', {'invoices': invoices})

# Display contents of the requested invoice
@login_required
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    return render(request, 'invoice/invoice_detail.html', {'invoice': invoice})

# Invoice summary
@login_required
def invoice_summary(request):
    total_invoices = Invoice.objects.count()
    total_paid_invoices = Invoice.objects.filter(paid=True).count()
    total_unpaid_invoices = Invoice.objects.filter(paid=False).count()

    return {
        'total_invoices': total_invoices,
        'total_paid_invoices' : total_paid_invoices,
        'total_unpaid_invoices' : total_unpaid_invoices,
    }

# Dashboard function
@login_required
def dashboard(request):
    # Get invoice summary data
    summary_data = invoice_summary(request)

    """
    total_amount = 0
    paid_invoices = Invoice.objects.filter(paid=True)
    for invoice in paid_invoices:
        total_amount += invoice.total_cost

        'total_amount':total_amount
    """
    total_amount = sum(invoice.total_cost for invoice in Invoice.objects.filter(paid=True))
    ['total_amount'] or 0
    context = {
        'total_amount':total_amount
    }
    context.update(summary_data)
    return render(request, 'dashboard.html', context)

# Change invoice payment status to paid
@login_required
def mark_as_paid(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    invoice.paid = True
    invoice.save()
    return redirect('invoicing_app:invoice_detail', invoice_id=invoice.id)

# Change invoice payment status to unpaid
@login_required
def mark_as_unpaid(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    invoice.paid = False
    invoice.save()
    return redirect('invoicing_app:invoice_detail', invoice_id=invoice.id)

# Create Client
@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.created_by = request.user
            client.save()
            return redirect('invoicing_app:client_list')  # Assuming you have a client list view
        else:
            print(form.errors)
            # return render(request, 'client/create_client.html', {'form':form})
    else:
        form = ClientForm()

    return render(request, 'client/create_client.html', {'form': form})

# Edit client
@login_required
def edit_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client updated successfully!')
            return redirect('client_list')  # Assuming you have a client list view
        else:
            messages.error(request, 'Error updating client')
    else:
        form = ClientForm(instance=client)

    return render(request, 'clent/edit_client.html', {'form': form})

# Delete client
@login_required
def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Client deleted successfully!')
        return redirect('invoicing_app:client_list')

    return render(request, 'client/confirm_delete_client.html', {'client': client})

# Client list
@login_required
def client_list(request):
    client_list = Client.objects.all()
    paginator = Paginator(client_list, 10)

    page = request.GET.get('page')
    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('client/paginated_clients.html', {'clients':clients})
        data = {
            'html':html,
            'page_number': clients.number,
            'num_pages': paginator.num_pages,
            'total_items': paginator.count,
            'has_previous': clients.has_previous(),
            'has_next': clients.has_next(),
        }
        return JsonResponse(data)

    return render(request, 'client/client_list.html', {'clients':clients})

# Settings function
def edit_settings(request):
    settings_instance = Settings.objects.first()

    if request.method == 'POST':
        form = SettingsForm(request.POST, instance=settings_instance)
        if form.is_valid():
            form.save()
            return redirect('settings/settings_overview.html') # Redirect to settings page
        else:
            form = SettingsForm(instance=settings_instance)

        context = {
            'form': form,
            'settings_instance': settings_instance,
        }
        return render(request, 'invoice/settings.html', context)

# Settings overview
#def settings(request):
#    settings = Settings.objects.all()
#    return render(request, 'settings/settings_overview.html', {'settings':settings})
    
# Active client list
def active_clients_list(request):
    # Retrieve clients with client_status set to active
    active_clients = Client.objects.filter(active_status=True)
    
    # Render the template with the context
    return render(request, 'clients/active_clients_list.html', {'clients':active_clients})

# Active status
def mark_client_active(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.client_status = 'active'
    client.save()
    return redirect('clients_list')  # Adjust the redirect URL as needed

def mark_client_inactive(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.client_status = 'inactive'
    client.save()
    return redirect('clients_list')  # Adjust the redirect URL as needed

# Countries list function
def country(request):
    country_list = list(countries)
    return render(request, 'client/create_client.html', {'countries':country_list})