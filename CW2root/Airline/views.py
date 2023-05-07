from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .models import Airline, Airport, Flight, Booking
from datetime import timedelta
import requests
import json

def index(request):
    return HttpResponse("<h1>The means</h1>")

@csrf_exempt
#Adding New bookings:   
def newBooking(request):
        #Receiving Booking information:
        passport_number = request.POST.get("passport_number")
        bookingRef = request.POST.get("booking_ref")
        flightCode = request.POST.get("flight_code")
        flight = Flight.objects.get(flight_code = flightCode)
        if flight:
            #Saving Booking information in the database:
            Booking.objects.create(bookingRef = bookingRef ,passport_number = passport_number, flight = flight)

            #Update number of available seats in the database:
            flight.available_seats = flight.available_seats-1
            flight.save()

            return HttpResponse("New Booking saved", status = 204)
        else:
            return HttpResponse("The flight Code does not exist", status = 404)


@csrf_exempt
#Cancel a booking:  
def cancelBooking(request, BookingRef):

    #Retreiving the booking to cancel:
    booking = Booking.objects.get(bookingRef = BookingRef)

    if booking:
        booking.delete()
        return HttpResponse("The booking has been deleted", status = 204)
    else:
        return HttpResponse("This booking does not exist in teh database", status = 404)















@csrf_exempt
def bookings(request, BookingRef):
    if request.method == "POST":
        a = newBooking(request, BookingRef)
        if a == True: 
            return HttpResponse("New Booking saved", status = 204)
        else:
            return HttpResponse("Could not save the booking", status = 404)
    elif request.method == "DELETE":
        cancelBooking(request, BookingRef)
    else:
        
        return HttpResponse("New Booking saved", status = 204)




"""
#Sends a list of all available flights to the Aviation Authorities:
def availableFlights(request):
    if request.method == 'GET':
        flight_list = []
        flights = Flight.objects.filter(available_seats__gt=0)

        #Saves all the flights as a list of dictionaries.
        for f in flights:
            duration_time = f.duration_time.seconds
            data = {
                    "flight_code": f.flight_code,
                    "departure_date_time": f.departure_date_time.isoformat(),
                    "arrival_date_time": f.arrival_date_time.isoformat(),
                    "duration_time": duration_time,
                    "base_price": f.base_price,
                    "total_seats": f.total_seats,
                    "available_seats": f.available_seats,
                    "airline": f.airline.name,
                    "departure_airport": f.departure_airport.name,
                    "destination_airport": f.destination_airport.name,
                }
            flight_list.append(data)

        return JsonResponse({'ListofFlights': flight_list})
    else:
        return HttpResponseNotAllowed(['GET'])"""
    







