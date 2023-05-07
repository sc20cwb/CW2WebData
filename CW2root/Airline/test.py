from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta
import requests
import json
import requests

url_bookinggg = "http://127.0.0.1:8000/booking/BB12"
"""
data = {
    "PassportNumber": 12345678,
    "BookingRef": "BB12",
    "FlightCode": "CWB123",
}

r = requests.post(url_bookinggg, data=data)

if r.status_code == 204: 
    print("Flight send successfylly")
else:
    print(r.status_code)
    print("Unsuccessfull")
"""
r = requests.delete(url_bookinggg)

if r.status_code == 204:
    print("Booking cancelled successfully")
else:
    print("Failed to cancel booking")


def newFlights(request):
    if request.method == "POST":
        FlightCode = request.POST.get("FlighCode")
        DepartureDateTime = request.POST.get("DepartureDateTime")
        ArrivalDateTime = request.POST.get("ArrivalDateTime")
        DurationTime = request.POST.get("DurationTime")
        BasePrice = request.POST.get("BasePrice")
        TotalSeats = request.POST.get("TotalSeats")
        AvailableSeats = request.POST.get("AvailableSeats")
        AirlineName = request.POST.get("AirlineName")
        DepartureAirport = request.POST.get("DepartureAirport")
        DestinationAirport = request.POST.get("DestinationAirport")   


