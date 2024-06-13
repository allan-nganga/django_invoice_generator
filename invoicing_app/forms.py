from django import forms
from.models import Invoice, Client, InvoiceItem, Settings

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

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'due_date',  
            'client', 
            'paid'
        ]

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = [
            'description',
            'quantity',
            'price'
        ]

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