from django.contrib import admin
from .models import Departments,Doctors,Bookings,register
# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):                                        # to show database in table form for booking
    list_display=('id','Patient_name','Patient_email','Doctor_name')
class RegisterAdmin(admin.ModelAdmin):                                        # to show database in table form for booking
    list_display=('FullName','Email','Username','Password1','Password2')
    
admin.site.register(Bookings,BookingAdmin)
admin.site.register(register,RegisterAdmin)