from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product, Contact
 #Create your views here.


def home(request):
        return render(request, 'home.html')


def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2 = request.POST['pass2']
       

        if len(username) > 10:
            messages.error(request, 'Username more than 10 characters')
            return redirect('home')

        if not username.isalnum():
            messages.error(request, 'Username should only contain letters and numbers')
            return redirect('home')

        if pass1 != pass2 :
            messages.error(request, 'passwords do not match')
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'You account successfully created')
        return redirect('home')
    else:
        return HttpResponse('error 404 - not found')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        
        user = authenticate( username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Succesfully Logged in')
            return redirect('productview')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('home')
        
    else:
        return HttpResponse('error 404 - not found')


def handleLogout(request):
    logout(request)
    messages.success(request, 'Succesfully Logged out')
    return redirect('home')
        
def productview(request):  
    products = Product.objects.all()
   
    n = len(products)
    params = {'product': products, 'no_of_product': n}
    return render(request, 'product.html', params)

def contact(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        college = request.POST['college']
        cgpa = request.POST['cgpa']
        startup = request.POST['startup']
        contact = Contact(username = username, fname = fname, lname = lname, email=email, college=college,cgpa = cgpa, startup=startup)
        contact.save()
        messages.success(request, 'Succesfully Applied for internship')
        return redirect('productview')
    else:
        return render(request, 'contact.html')


def handlestartupLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['startuploginusername']
        loginpassword = request.POST['startuploginpassword']
        
        user = authenticate( username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Succesfully Logged in')
            return redirect('startup')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('home')
        
    else:
        return HttpResponse('error 404 - not found')

def startup(request):  
    
    contacts = Contact.objects.all()
    
    
    parameters = {'contact':contacts}
    
    return render(request, 'startup.html', parameters)

