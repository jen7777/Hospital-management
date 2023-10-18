from django.contrib import admin
from .models import Departments,Doctors,Bookings,login,Contact
# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Contact)
class BookingAdmin(admin.ModelAdmin):                                        # to show database in table form for booking
    list_display=('id','Patient_name','Patient_email','Doctor_name')
class LoginAdmin(admin.ModelAdmin):                                        # to show database in table form for booking
    list_display=('Username','Password1')
    
admin.site.register(Bookings,BookingAdmin)
admin.site.register(login,LoginAdmin)