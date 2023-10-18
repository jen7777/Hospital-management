from django.urls import path,include
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name='home'),
path('bookings/',views.bookings,name='bookings'),
path('doctors/',views.doctors,name='doctors'),
path('contacts/',views.contact,name='contacts'),
path('departments/',views.departments,name='departments'),
path('register/',views.register,name='register'),
path('login/',views.login,name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)          #pic serving