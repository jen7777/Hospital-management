from django.db import models

# this is database
# Always migrate in terminal and register in admin.py after any change in models.py

class Departments(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()
    def __str__(self):
        return self.dep_name            #to display actualdepartment name in admin

class Doctors(models.Model):
    doc_name=models.CharField(max_length=255)
    doc_spec=models.CharField(max_length=255)
    doc_dep=models.ForeignKey(Departments,on_delete=models.CASCADE)  #dropdown to select, deleting removes doctor
    doc_image=models.ImageField(upload_to='doctors')                #install pillow to upload pic
    def __str__(self):
        return self.doc_name

class Bookings(models.Model):
    Patient_name=models.CharField(max_length=255)
    Patient_email=models.EmailField()
    Doctor_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    Booking_date=models.DateField()
    def __str__(self):
        return 'self.doc_name' 
    
class register(models.Model):
    FullName=models.CharField(max_length=255)
    Email=models.EmailField()
    Username=models.CharField(max_length=255)
    Password1=models.CharField(max_length=255)
    Password2=models.CharField(max_length=255)
