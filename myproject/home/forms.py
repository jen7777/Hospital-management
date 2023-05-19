from django import forms 
from .models import Bookings,register,login
class DateInput(forms.DateInput):
        input_type='date'
        
class Bookingform(forms.ModelForm):
    
    
    class Meta:
        model=Bookings
        fields='__all__'
        
        widgets={
            'Booking_date': DateInput(),     #colon for dictionary
        }
        labels={
            'Patient_name' : "Patient name",
            'Patient_email': "Patient email",
            'Doctor_name'  : "Doctor name",
            'Booking_date' : "Booking date",
        }

class CreateUserForm(forms.ModelForm):
    
    class Meta:
        model=register
        fields=['FullName','Email','Username','Password1','Password2']
        
        labels={
            'FullName': "Full Name",
            'Email': "Email",
            'Username':"Username",
            'Password1':"Password",
            'Password2':"Confirm Password",
        }
    
class LoginForm(forms.ModelForm):
    
    class Meta:
        model=login
        fields='__all__'
        
        labels={
            'Username':"Username",
            'Password1':"Password",
        }