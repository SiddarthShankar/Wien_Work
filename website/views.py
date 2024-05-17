from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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