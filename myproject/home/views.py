from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors,Contact
from .forms import Bookingform,CreateUserForm,LoginForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,'home.html')      #or return HttpResponse("Home")

def bookings(request):
    if request.method=="POST":
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'We recieved your booking request')
             
    form=Bookingform()
    dict_form={
        'form' : form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    dict_doc={
        'doc' : Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doc)

def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')               #name input by user is copied to variable name
        email=request.POST.get('email')
        message=request.POST.get('message')
                                                    
        contact.name=name                           #name from variable name is copied to contact.name model(backend)
        contact.email=email
        contact.message=message
        contact.save()                              #saving backend model class contact
        return HttpResponse("Thanks")
    return render(request,'contact.html')

def departments(request):
    dict_dept={
        'dept': Departments.objects.all()         #pull all objects from class dept
    }
    return render(request,'departments.html',dict_dept)
  
def register(request):
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        p1=request.POST.get('Password1')
        p2=request.POST.get('Password2')
        if form.is_valid():
                form.save()
                return render(request,'confirmation.html')
             
    form=CreateUserForm()
    dict_form={
        'form' : form
    }
    return render(request,'register.html',dict_form)
    
def login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        Username=request.POST.get('Username')
        Password=request.POST.get('Password1')
        user=authenticate(request,username=Username,password=Password)
        if user is not None:
                return render(request,'home.html')
        else:
            messages.warning(request,'Incorrect username or password')     
    form=LoginForm()
    dict_form={
        'form' : form
    }
    return render(request,'login.html',dict_form)
    