from django.contrib import admin
from .models import Airline, Airport, Flight, Booking
from django import forms
from django.core.exceptions import ValidationError

class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class AirportAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)

class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_code',)
    ordering = ('flight_code',)
    search_fields = ('flight_code',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('bookingRef',)
    ordering = ('bookingRef',)
    search_fields = ('bookingRef',)

admin.site.register(Airline, AirlineAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Booking, BookingAdmin)