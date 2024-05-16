from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
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
        return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully Logged Out!!....")
    return redirect('home')
