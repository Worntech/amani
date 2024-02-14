from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User, auth
from . models import *
from . forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from django.conf import settings

from sims.views import *

# Create your views here.
# @login_required(login_url='signin')
def admin(request):
    return render(request, 'web/admin.html')
def signup(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('signup')
            elif MyUser.objects.filter(username=username).exists():
                messages.info(request, f"Username {username} Already Taken")
                return redirect('signup')
            else:
                user = MyUser.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                user.save()
                # messages.info(request, 'Registered succesefull.')
                return redirect('signupsucces')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('signup')

    else:
        return render(request, 'web/signup.html')

def signin(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.info(request, 'Loged in succesefull.')
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('signin')

    else:
        return render(request, 'web/signin.html')

def logout(request):
    auth.logout(request)
    # messages.info(request, 'Loged out succesefull.')
    return redirect('logedout')


def home(request):
    return render(request, 'web/home.html')
def aboutus(request):
    return render(request, 'web/aboutus.html')
def base(request):
    return render(request, 'web/base.html')
def contactus(request):
    return render(request, 'web/contactus.html')
def contactpost(request):
    contactpost = ContactForm()
    if request.method == "POST":
        Full_Name = request.POST.get('name')
        Subject = request.POST.get('subject')
        Email = request.POST.get('email')
        Message = request.POST.get('message')
        Phone = request.POST.get('phone')
        contactpost = ContactForm(request.POST, files=request.FILES)
        if contactpost.is_valid():
            contactpost.save()
            messages.info(request, 'Message sent succesefull.')
            return redirect('contactpost')
    context={
        "contactpost":contactpost
    }
    return render(request, 'web/contactpost.html',context)
# @login_required(login_url='signin')
def contactlist(request):
    contactlist = Contact.objects.all()
    countmessage= Contact.objects.all().count()
    context={
        "contactlist":contactlist,
        "countmessage":countmessage
    }
    return render(request, 'web/contactlist.html', context)
# @login_required(login_url='signin')
def viewcontact(request, id):
    contact = Contact.objects.get(id=id)
    
    context = {"contact":contact}
    return render(request, 'web/viewcontact.html', context)
# @login_required(login_url='signin')
def deletecontact(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == "POST":
        contact.delete()
        messages.info(request, 'Message deleted succesefull.')
        return redirect('contactlist')
    
    context = {"contact":contact}
    return render(request, 'web/deletecontact.html', context)


# @login_required(login_url='signin')
def dashboard(request):
    return render(request, 'web/dashboard.html')

def services(request):
    return render(request, 'web/services.html')


# views for success message
def signupsucces(request):
    return render(request, 'web/signupsucces.html')
def logedout(request):
    return render(request, 'web/logedout.html')


def invoices(request):
    return render(request, 'web/invoices.html')
def payments(request):
    return render(request, 'web/payments.html')


def allstaff(request):
    return render(request, 'web/allstaff.html')
def courses(request):
    return render(request, 'web/courses.html')
