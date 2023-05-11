from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Airline, Airport, Flight, Booking
from datetime import timedelta
import requests
import json

def index(request):
    return HttpResponse("<h1>API Airlines</h1>", status = 200)


@csrf_exempt
#Adding New bookings:   
def newBooking(request):
        #Receiving Booking information:
        passport_number = request.POST.get("passport_number")
        bookingRef = request.POST.get("booking_ref")
        flightCode = request.POST.get("flight")
        try: 
            flight = Flight.objects.get(flight_code = flightCode)
            if flight:
                #Saving Booking information in the database:
                Booking.objects.create(bookingRef = bookingRef ,passport_number = passport_number, flight = flight)

                #Update number of available seats in the database:
                flight.available_seats -= 1
                super(Flight, flight).save()
                return True
            else:
                return False
        except Flight.DoesNotExist:
            return False
        except: 
            return False

            
        
@csrf_exempt
#Cancel a booking:  
def cancelBooking(request):

    #Retreiving the booking to cancel:
    booking = Booking.objects.get(bookingRef = request.GET.get('booking_ref'))
    print(request.GET.get('booking_ref'))
    flight = booking.flight
    flight.available_seats +=1
    super(Flight, flight).save()
    
    if booking:
        booking.delete()
        return True
    else:
        return False


@csrf_exempt
def booking(request):
    if request.method == "POST":
        a  = newBooking(request)
        if a == True: 
            return HttpResponse("New Booking saved.", status = 204)
        else:
            return HttpResponse("Could not save the booking", status = 404)
    elif request.method == "DELETE":
        a = cancelBooking(request)
        if a ==True:
            return HttpResponse("Booking deleted successfully.", status = 204)
        else: 
            return HttpResponse("Could not delete the booking.", status = 400)
        

@api_view(['PATCH', 'POST', 'DELETE'])
@csrf_exempt     
def newFlights(request):
    if request.method == "POST":
        FlightCode = request.data.get("fligh_code")
        DepartureDateTime = request.data.get("departure_datetime")
        ArrivalDateTime = request.data.get("arrival_datetime")
        DurationTime = request.data.get("duration_time")
        BasePrice = request.data.get("base_price")
        TotalSeats = request.data.get("total_seats")
        AvailableSeats = request.data.get("available_seats")
        AirlineName = request.data.get("airline")
        DepartureAirport = request.data.get("departure_airport")
        DestinationAirport = request.data.get("destination_airport")  

        print(AirlineName)
        print(DepartureAirport)
        print(DestinationAirport)
        return HttpResponse("DATA.", status = 201)
    elif request.method == "PATCH":

        FlightCode = request.data.get("fligh_code")
        DepartureDateTime = request.data.get("departure_datetime")
        ArrivalDateTime = request.data.get("arrival_datetime")
        DurationTime = request.data.get("duration_time")
        BasePrice = request.data.get("base_price")
        TotalSeats = request.data.get("total_seats")
        AvailableSeats = request.data.get("available_seats")
        AirlineName = request.data.get("airline")
        DepartureAirport = request.data.get("departure_airport")
        DestinationAirport = request.data.get("destination_airport") 

        print(AirlineName)
        print(DepartureAirport)
        print(DestinationAirport)

        return HttpResponse(" PATCH DATA.", status = 200)
    elif request.method == "DELETE":
        f = Flight.objects.get(flight_code = request.GET.get('flight_code'))
        print(f)
        print(request.GET.get('flight_code'))
        return HttpResponse("DELETE DATA.", status = 200)
    else:
        return HttpResponse("NO DATA.", status = 404) 


    







