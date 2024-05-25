from django.db import models

# Create your models here.
class Invoice(models.Model):
    company_name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=200)
    billing_address = models.CharField(max_length=200)
    item_description = models.TextField()
    item_quantity = models.IntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice #{self.id} for {self.client_name}"
    
    @property
    def total_cost(self):
        return self.item_quantity * self.item_price