from django.db import models
import phonenumbers
from django.core.validators import ValidationError
import requests
from datetime import timedelta


# Create your models here.

class Airline(models.Model):
    code = models.CharField(max_length=15 ,unique=True)
    name = models.CharField(max_length=60 ,unique=True)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=17 ,unique=True)

    def clean(self):
        num = phonenumbers.parse(self.phone, None)
        if not phonenumbers.is_valid_number(num):
            raise ValidationError('Not a vlaid phone number')
        
    def __str__(self):
        return self.name

class Airport(models.Model):
    name = models.CharField(max_length=60,unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Flight(models.Model):
    flight_code = models.CharField(max_length=10, unique=True)
    departure_date_time = models.DateTimeField(auto_now=False)
    arrival_date_time = models.DateTimeField(auto_now=False)
    duration_time = models.DurationField()
    base_price = models.FloatField()
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='flights')
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')

    def save(self, *args, **kwargs):

        url_update_Aviation_Authority = "http://api/flights/"
        is_new_flight = self._state.adding

        if is_new_flight:
            duration_time = self.duration_time.seconds
            
            data = {
                "flight_code": self.flight_code, 
                "departure_dateTime": self.departure_date_time,
                "arrival_dateTime": self.arrival_date_time,
                "duration_Time": duration_time,
                "base_price": self.base_price,
                "total_seats": self.total_seats,
                "available_seats": self.available_seats,
                "airline_name": self.airline,
                "departure_airport": self.departure_airport,
                "destination_airport": self.destination_airport,
            }
            r = requests.post(url_update_Aviation_Authority, data=data)
            if r.status_code == 204:
                print("Flight sent successfully")
                super(Flight, self).save(*args, **kwargs)
            else:
                print("Unsuccessfull")
        else:
            data = {
                "flight_code": self.flight_code, 
                "departure_dateTime": self.departure_date_time,
                "arrival_dateTime": self.arrival_date_time,
                "duration_Time": duration_time,
                "base_price": self.base_price,
                "total_seats": self.total_seats,
                "available_seats": self.available_seats,
                "airline_name": self.airline,
                "departure_airport": self.departure_airport,
                "destination_airport": self.destination_airport,
            }
            r = requests.patch(url_update_Aviation_Authority, data=data)

            if r.status_code == 204:
                super(Flight, self).save(*args, **kwargs)
                print("Flight sent successfully")
            else:
                print("Unsuccessfull")

    def delete(self, using=None, keep_parents=False):
        url = f'https://api/flight/?flight_code={self.flight_code}'
        response = requests.delete(url)

        if response.status_code == 204:
            super().delete(using=using, keep_parents=keep_parents)
            print('flight deleted.')
        else:
            print('The flight was not deleted.')

    def __str__(self):
        return self.airline.name
    

class Booking(models.Model):
    bookingRef = models.CharField(unique=True, max_length= 20)
    passport_number = models.IntegerField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='bookings')

    def __str__(self):
        return self.bookingRef

