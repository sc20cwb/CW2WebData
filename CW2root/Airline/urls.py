from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('api/bookings/', views.booking, name='Bookings'),
    path('api/test/', views.newFlights, name='NewFlights'),
       
]