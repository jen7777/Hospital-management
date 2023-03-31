from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='home'),
path('about/',views.about,name='about'),
path('bookings/',views.booking,name='bookings'),
path('doctors/',views.doctors,name='doctors'),
path('contacts/',views.contact,name='contacts'),
path('departments/',views.departments,name='departments')

]