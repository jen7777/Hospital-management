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
    doc_dep=models.ForeignKey(Departments,on_delete=models.CASCADE)  #dropdown to select
    doc_image=models.ImageField(upload_to='doctors')                #install pillow to upload pic
    def __str__(self):
        return self.doc_name

class Bookings(models.Model):
    p_name=models.CharField(max_length=255)
    p_phone=models.CharField(max_length=12)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    Booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
    def __str__(self):
        return 'Dr' + self.doc_name
