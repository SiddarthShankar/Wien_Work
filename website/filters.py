import django_filters 
from .models import *

class OrderFilter(django_filters.FilterSet):
    class meta:
        model = Customer
        fields = '__all__'