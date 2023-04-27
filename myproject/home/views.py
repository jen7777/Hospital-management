from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import Bookingform
# Create your views here.
def index(request):
    return render(request,'home.html')      #or return HttpResponse("Home")
def about(request):
    return render(request,'about.html')

def bookings(request):
    if request.method=="POST":
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
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
    return render(request,'contact.html')

def departments(request):
    dict_dept={
        'dept': Departments.objects.all()         #pull all objects from class dept
    }
    return render(request,'departments.html',dict_dept)