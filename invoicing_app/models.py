from django.db import models
import uuid
from django_countries.fields import CountryField
from django.contrib.auth.models import User


# Create your models here.
class Client(models.Model):
    client_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_name = models.CharField(max_length=255)
    client_address = models.TextField(null=True, blank=True)  # Nullable field
    client_email = models.EmailField(null=True, blank=True)  # Nullable field
    client_company_name = models.CharField(max_length=255)
    active_status = models.BooleanField(default=True)
    client_country = CountryField(blank_label='(select country)', default='Kenya')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_created_by')
    created_at = models.DateTimeField(auto_now_add=True)

    # owned_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='client_owned_by', default=User)

    def __str__(self):
        return self.client_name


class Invoice(models.Model):
    invoice_id = models.CharField(max_length=100, unique=True, blank=True)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoice_created_by', default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice #{self.id} for {self.client.client_name}"

    @property
    def total_cost(self):
        return sum(item.quantity * item.price for item in self.items.all())
    
    # For invoice to be saved using unique id
    def save(self, *args, **kwargs):
        if not self.invoice_id:
            self.invoice_id = str(uuid.uuid4())
        super().save(*args, **kwargs)


class InvoiceItem(models.Model):
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(null=True)
    quantity = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoice_item_created_by', default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Item {self.id} of Invoice {self.invoice.id}"


class Settings(models.Model):
    company_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)  # Nullable field
    company_email = models.EmailField(null=True, blank=True)  # Nullable field
    company_address = models.TextField(null=True, blank=True)  # Nullable field
    company_city = models.CharField(max_length=255, null=True, blank=True)  # Nullable field
    company_country = CountryField(blank_label='(select country)', default='Kenya')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_created_by', default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name