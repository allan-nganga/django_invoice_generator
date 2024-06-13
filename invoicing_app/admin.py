from django.contrib import admin
from .models import Invoice, InvoiceItem, Client, Settings

# Register your models here.
admin.site.register(Invoice)
admin.site.register(Client)
admin.site.register(InvoiceItem)
admin.site.register(Settings)