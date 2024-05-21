from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddRecordForm
from .models import Customer

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    
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
        return render(request, 'home.html', {'customers': customers})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully Logged Out!!....")
    return redirect('home')

def customer_order(request, pk):
    if request.user.is_authenticated:
        #look up records
        customer_order = Customer.objects.get(id=pk)
        return render(request, 'order.html', {'customer_order':customer_order})
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
    
def delete_details(request, pk):
    if request.user.is_authenticated:
        delete_detail = Customer.objects.get(id=pk)
        delete_detail.delete()
        messages.success(request, "Details have been deleted successfully!!..")
        return redirect('home') 
    else:
        messages.success(request, "You must be logged into access the data")
        return redirect('home') 

def add_details(request):
    customer_form = AddRecordForm(request.POST or None) 
    if request.user.is_authenticated:
        if request.method == "POST":
            if customer_form.is_valid():
                add_details = customer_form.save()
                messages.success(request, "Details added successfully!!...")
                return redirect('home')
        return render(request, 'add_details.html', {'customer_form':customer_form})
    else:
        messages.success(request, "You must be logged in to add a form")
        return redirect('home') 
    
def update_details(request, pk):
    if request.user.is_authenticated:
        current_detail = Customer.objects.get(id=pk)
        customer_form = AddRecordForm(request.POST or None, instance=current_detail)
        if customer_form.is_valid():
            customer_form.save() 
            messages.success(request, "Details have been Updated successfully!!..")
            return redirect('home') 
        return render(request, 'update_details.html', {'customer_form':customer_form})
    else:
        messages.success(request, "You must be logged into access the data")
        return redirect('home') 