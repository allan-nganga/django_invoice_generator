from django import forms
from.models import Invoice, Client, InvoiceItem, Settings
from django_countries.widgets import CountrySelectWidget
from django.forms import inlineformset_factory

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'client_name',
            'client_address',
            'client_email',
            'client_company_name',
            'active_status',
            'client_country'
        ]
        widgets = {
            'client_country':CountrySelectWidget(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
            })
        }

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'due_date',  
            'client', 
            'paid'
        ]
    client = forms.ModelChoiceField(
        queryset=Client.objects.filter(active_status=True),
        empty_label="Select Client"
    )

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = [
            'description',
            'quantity',
            'price'
        ]
InvoiceItemFormSet = inlineformset_factory(Invoice, InvoiceItem, form=InvoiceItemForm, extra=1)

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = [
            'company_name',
            'logo',
            'company_email',
            'company_address',
            'company_city',
            'company_country'
        ]
        widgets = {
            'company_country':CountrySelectWidget(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
            })
        }