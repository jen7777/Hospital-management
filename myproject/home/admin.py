from django.contrib import admin
from .models import Departments,Doctors,Bookings
# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):                                        # to show database in table form for booking
    list_display=('id','Patient_name','Patient_email','Doctor_name')
    
admin.site.register(Bookings,BookingAdmin)