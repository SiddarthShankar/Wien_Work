import django_filters 
from .models import *

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = {'customer_num', 'first_name', 'last_name'}
        
class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['status']