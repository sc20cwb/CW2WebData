from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking', views.newBooking, name='NewBooking'),
    path('booking/<str:BookingRef>/', views.cancelBooking, name='DeleteBooking'),
    
]