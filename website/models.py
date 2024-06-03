from django.db import models

# Create your models here.
class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    customer_num = models.IntegerField()
    order_num = models.IntegerField()
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=15, null=True)
    
    def __str__(self):
        return(f"{self.first_name} {self.last_name}")

class Order(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('Ready for dispatch', 'Ready for dispatch'),
            ('Out for delivery', 'Out for delivery'),
            ('Delivered', 'Delivered'),
    )
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    def __str__(self):
        return f"Order {self.id} for Customer {self.customer_id}"
