from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddCustomerRecordForm, AddOrderRecordForm, OrderStatusForm
from .models import Customer, Order
from .filters import OrderFilter, CustomerFilter
from django.utils.translation import gettext as _
from django.utils import translation
from django.conf import settings

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    myFilters = CustomerFilter(request.GET, queryset=customers)
    customers = myFilters.qs
    
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    
    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending, 'myFilters': myFilters}
    
    if request.method == 'GET' and 'order_id' in request.GET:
        order_id = request.GET.get('order_id')
        if order_id:
            try:
                order = Order.objects.get(id=order_id)
                return redirect('order_Details', pk=order.id)
            except Order.DoesNotExist:
                messages.error(request, _("Order not found!"))
    
    #check to see if logging in 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Authentication step 
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, _("You have been successfully logged in!!!!...."))
            return redirect('home')
        else:
            messages.success(request, _("An error occured, please try again!!...."))
            return redirect('home')
    else:   
        return render(request, 'home.html', context)

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, _("You have been successfully Logged Out!!...."))
    return redirect('home')

def customer_order(request, pk):
    if request.user.is_authenticated:
        # Look up records
        orders = Order.objects.all()
        customer_order = Customer.objects.get(id=pk)
        customer_num = Customer.objects.get(id=pk)
        order_Details = Order.objects.filter(customer_id=pk)
        
        myFilters = OrderFilter(request.GET, queryset=orders)
        orders = myFilters.qs
        
        context = {
            'customer_num':customer_num,
            'order_Details': order_Details,
            'customer_order': customer_order,
            'orders': orders,
            'myFilters': myFilters
        }
        return render(request, 'order.html', context)
    else:
        messages.success(request, _("You must be logged into access the data"))
        return redirect('home')

def customer_num(request, pk):
    if request.user.is_authenticated:
        customer_num = Customer.objects.get(id=pk)
        order_Details = Order.objects.filter(customer_id=pk)
        context = {
            'customer_num':customer_num,
            'order_Details': order_Details,
        }
        return render(request, 'customer.html', context)
    else:
        messages.success(request, _("You must be logged into access the data"))
        return redirect('home') 
   
def delete_CustomerDetails(request, pk):
    if request.user.is_authenticated:
        delete_detail = Customer.objects.get(id=pk)
        delete_detail.delete()
        messages.success(request, _("Details have been deleted successfully!!.."))
        return redirect('home') 
    else:
        messages.success(request, _("You must be logged into access the data"))
        return redirect('home') 

def add_CustomerDetails(request):
    customer_form = AddCustomerRecordForm(request.POST or None) 
    if request.user.is_authenticated:
        if request.method == "POST":
            if customer_form.is_valid():
                add_details = customer_form.save()
                messages.success(request, _("Details added successfully!!..."))
                return redirect('home')
        return render(request, 'add_CustomerDetails.html', {'customer_form':customer_form})
    else:
        messages.success(request, _("You must be logged in to add a form"))
        return redirect('home') 
    
def update_CustomerDetails(request, pk):
    if request.user.is_authenticated:
        current_detail = Customer.objects.get(id=pk)
        customer_form = AddCustomerRecordForm(request.POST or None, instance=current_detail)
        if customer_form.is_valid():
            customer_form.save() 
            messages.success(request, _("Details have been Updated successfully!!.."))
            return redirect('home') 
        return render(request, 'update_CustomerDetails.html', {'customer_form':customer_form})
    else:
        messages.success(request, _("You must be logged into access the data"))
        return redirect('home') 

def delete_OrderDetails(request, pk):
    if request.user.is_authenticated:
        delete_order = get_object_or_404(Order, id=pk)
        delete_order.delete()
        messages.success(request, _("Details have been deleted successfully!!.."))
        return redirect('home') 
    else:
        messages.success(request, _("You must be logged into access the data"))
        return redirect('home') 

def add_OrderDetails(request):
    order_form = AddOrderRecordForm(request.POST or None) 
    if request.user.is_authenticated:
        if request.method == "POST":
            if order_form.is_valid():
                order_form.save()
                messages.success(request, _("Details added successfully!!..."))
                return redirect('/')
        return render(request, 'add_OrderDetails.html', {'order_form':order_form})
    else:
        messages.success(request, _("You must be logged in to add a form"))
        return redirect('home')   
    
def update_OrderDetails(request, pk):
    if request.user.is_authenticated:
        current_detail = get_object_or_404(Order, id=pk)
        order_form = AddOrderRecordForm(request.POST or None, instance=current_detail)
        if request.method == 'POST':
            if order_form.is_valid():
                order_form.save()
                messages.success(request, _("Details have been updated successfully!"))
                return redirect('/')
            else:
                # Show errors if form is invalid
                messages.error(request, _("There was an error updating the details. Please check the form for errors."))
        return render(request, 'update_OrderDetails.html', {'order_form': order_form})
    else:
        messages.error(request, _("You must be logged in to access the data"))
        return redirect('home')
    
def about(request):
    if request.user.is_authenticated:
        return render(request, 'about.html', {'about':about})
    else:
        messages.success(request, _("You must be logged into access the data"))
        return redirect('home') 
    
def order_Details(request, pk):
    if request.user.is_authenticated:
        # Look up records
        orders = get_object_or_404(Order, id=pk)
        customer = orders.customer_id  # Correct attribute name
        context = {
            'customer': customer,
            'orders': orders,
        }
        return render(request, 'order_Details.html', context)
    else:
        messages.success(request, _("You must be logged in to view this order"))
        return redirect('home') 
    
def update_order_status(request, pk):
    if request.user.is_authenticated:
        order = get_object_or_404(Order, id=pk)
        if request.method == 'POST':
            form = OrderStatusForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                messages.success(request, _("Order status updated successfully!"))
            else:
                messages.error(request, _("Failed to update order status. Please try again."))
        return redirect('customer_order', pk=order.customer_id.id)
    else:
        messages.error(request, _("You must be logged in to update the order status"))
        return redirect('home')
    
def increase_font_size(request):
    current_size = request.session.get('font_size', 16)
    new_size = min(current_size + 2, 30)  # Increase by 2px, with a maximum size of 20px
    request.session['font_size'] = new_size
    return redirect(request.META.get('HTTP_REFERER', '/'))

def decrease_font_size(request):
    current_size = request.session.get('font_size', 16)
    new_size = max(current_size - 2, 12)  # Decrease by 2px, with a minimum size of 12px
    request.session['font_size'] = new_size
    return redirect(request.META.get('HTTP_REFERER', '/'))

def switch_theme(request, theme_name):
    request.session['theme'] = theme_name
    return redirect(request.META.get('HTTP_REFERER', '/'))

def switch_language(request):
    lang_code = request.GET.get('language', None) 
    next_url = request.GET.get('next', '/')
    if lang_code and lang_code in dict(settings.LANGUAGES).keys():
        translation.activate(lang_code)
        response = redirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        return response
    else:
        return redirect(next_url)
