from django.db import models
from models import Customer
from models import Order

#(1)Returns all customers from customer table
customers = Customer.objects.all()

#(2)Returns first customer in table 
firstCustomer = Customer.objects.first()

#(3)Returns last customer in table 
lastCustomer = Customer.objects.last()

#(4) Returns single customer by name 
customerByName = Customer.objects.get(name='Your Name')

##(5) Returns single customer by ID 
customerByName = Customer.objects.get(id=4)

#(6) Returns all orders related to customer
firstCustomerOrder = firstCustomer.order_set.all()

#(7) Returns orders customer-name(Query parent model value)
order = Order.objects.first()
parentName = Order.customer.name()


    
#Related set example

class ParentModel(models.Model):
    name = models.CharField(max_length = 200, null = True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null = True)
    
parent = ParentModel.objects.first()

#Returns all child models related to parent
parent.childmodel_set.all()

