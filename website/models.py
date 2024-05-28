from django.db import models

# Create your models here.
class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    order_num = models.IntegerField()
    customer_num = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    
    def __str__(self):
        return(f"Customer {self.first_name} {self.last_name} with order number {self.order_num}")
    