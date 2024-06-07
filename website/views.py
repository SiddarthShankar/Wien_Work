from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddCustomerRecordForm, AddOrderRecordForm, OrderStatusForm
from .models import Customer, Order

#from .filters import OrderFilter

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    
    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
    
    #check to see if logging in 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Authentication step 
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in!!!!....")
            return redirect('home')
        else:
            messages.success(request, "An error occured, please try again!!....")
            return redirect('home')
    else:   
        return render(request, 'home.html', context)

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully Logged Out!!....")
    return redirect('home')

def customer_order(request, pk):
    if request.user.is_authenticated:
        # Look up records
        orders = Order.objects.all()
        customer_order = Customer.objects.get(id=pk)
        
        # Merge the two dictionaries into one
        context = {
            'customer_order': customer_order,
            'orders': orders,
        }
        return render(request, 'order.html', context)
    else:
        messages.success(request, "You must be logged into access the data")
        return redirect('home')

def customer_num(request, pk):
    if request.user.is_authenticated:
        customer_num = Customer.objects.get(id=pk)
        return render(request, 'customer.html', {'customer_num':customer_num})
    else:
        messages.success(request, "You must be logged into access the data")
        return redirect('home') 
    
def delete_CustomerDetails(request, pk):
    if request.user.is_authenticated:
        delete_detail = Customer.objects.get(id=pk)
        delete_detail.delete()
        messages.success(request, "Details have been deleted successfully!!..")
        return redirect('home') 
    else:
        messages.success(request, "You must be logged into access the data")
        return redirect('home') 

def add_CustomerDetails(request):
    customer_form = AddCustomerRecordForm(request.POST or None) 
    if request.user.is_authenticated:
        if request.method == "POST":
            if customer_form.is_valid():
                add_details = customer_form.save()
                messages.success(request, "Details added successfully!!...")
                return redirect('home')
        return render(request, 'add_CustomerDetails.html', {'customer_form':customer_form})
    else:
        messages.success(request, "You must be logged in to add a form")
        return redirect('home') 
    
def update_CustomerDetails(request, pk):
    if request.user.is_authenticated:
        current_detail = Customer.objects.get(id=pk)
        customer_form = AddCustomerRecordForm(request.POST or None, instance=current_detail)
        if customer_form.is_valid():
            customer_form.save() 
            messages.success(request, "Details have been Updated successfully!!..")
            return redirect('home') 
        return render(request, 'update_CustomerDetails.html', {'customer_form':customer_form})
    else:
        messages.success(request, "You must be logged into access the data")
        return redirect('home') 

#def order(request):
#    if request.user.is_authenticated:
#       orders = Order.objects.all()
#       return render(request, 'order.html', {'orders': orders})
#   else:
#       messages.success(request, "You must be logged into access the data")
#       return redirect('home') 

def delete_OrderDetails(request, pk):
    if request.user.is_authenticated:
        delete_detail = Order.objects.get(id=pk)
        delete_detail.delete()
        messages.success(request, "Details have been deleted successfully!!..")
        return redirect('home') 
    else:
        messages.success(request, "You must be logged into access the data")
        return redirect('home') 

def add_OrderDetails(request):
    order_form = AddOrderRecordForm(request.POST or None) 
    if request.user.is_authenticated:
        if request.method == "POST":
            if order_form.is_valid():
                order_form.save()
                messages.success(request, "Details added successfully!!...")
                return redirect('/')
        return render(request, 'add_OrderDetails.html', {'order_form':order_form})
    else:
        messages.success(request, "You must be logged in to add a form")
        return redirect('home') 
    
def update_OrderDetails(request, pk):
    if request.user.is_authenticated:
        current_detail = Order.objects.get(id=pk)
        order_form = AddOrderRecordForm(request.POST or None, instance=current_detail)
        if order_form.is_valid():
            order_form.save() 
            messages.success(request, "Details have been Updated successfully!!..")
            return redirect('/') 
        return render(request, 'update_CustomerDetails.html', {'order_form':order_form})
    else:
        messages.success(request, "You must be logged into access the data")
        return redirect('home')        
    
def about(request):
    if request.user.is_authenticated:
        return render(request, 'about.html', {'about':about})
    else:
        messages.success(request, "You must be logged into access the data")
        return redirect('home') 