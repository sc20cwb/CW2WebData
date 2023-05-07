from django.contrib import admin
from .models import Airline, Airport, Flight, Booking

class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)

admin.site.register(Airline, AirlineAdmin)
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Booking)

