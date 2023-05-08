from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta
import requests
import json
import requests


url_bookinggg = "http://127.0.0.1:8000/bookings/"

data = {
    "passport_number": 12345678,
    "booking_ref": "BB12",
    "flight": "CWB123",
}

r = requests.post(url_bookinggg, data=data)

if r.status_code == 204: 
    print(r.status_code)
    print("New Booking saved")
    
else:
    print(r.status_code)
    print("Could not save the booking")

url_bookinggg = "http://127.0.0.1:8000/bookings/?booking_ref=BB12"

r = requests.delete(url_bookinggg)

if r.status_code == 204:
    print("Booking cancelled successfully")
else:
    print("Failed to cancel booking")





