from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('bookings/', views.booking, name='Bookings'),
    path('test/', views.newFlights, name='NewFlights'),
       
]