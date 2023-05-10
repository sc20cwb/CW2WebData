from django.test import TestCase, Client
from django.urls import reverse
from django.utils  import timezone
from datetime import timedelta
from Airline.models import Flight, Booking, Airline, Airport

class IndexViewTest(TestCase):

    def test_should_show_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>API Airlines</h1>")

class NewBookingTest(TestCase):

    def setUp(self):
        #Create Airline and Airport for testing.
        airline = Airline.objects.create(name='Test Airline', code = 'TT', country = 'United Kingdom', phone = "+44-800-101-111")
        departure_airport = Airport.objects.create(ident='AAA', name='Departure Airport', city = "Manchester", country = 'United Kingdom')
        destination_airport = Airport.objects.create(ident='BBB', name='Destination Airport', city = "Manchester", country = 'United Kingdom')
        self.flight = Flight.objects.create(
            flight_code='TT123',
            departure_date_time=timezone.now(),
            arrival_date_time=timezone.now() + timedelta(hours=2),
            duration_time=timedelta(hours=2),
            base_price=100,
            total_seats=100,
            available_seats=100,
            airline=airline,
            departure_airport=departure_airport,
            destination_airport=destination_airport,
        )

    def test_new_booking(self):
        data = {
            "passport_number": 12345678,
            "booking_ref": "BB12",
            "flight": self.flight.flight_code,}
        
        response = self.client.post(reverse('Bookings'), data)
        self.assertEqual(response.status_code, 204)
        booking = Booking.objects.filter(bookingRef='BB12', passport_number= 12345678, flight=self.flight)
        self.assertTrue(booking.exists())
        self.flight.refresh_from_db()
        self.assertEqual(self.flight.available_seats, 99)

    def test_new_booking_InvalidFlight(self):
        data = {
        
            "passport_number": 12345678,
            "booking_ref": "BB12",
            "flight": "INVALID",}
        
        response = self.client.post(reverse('Bookings'), data)
        self.assertEqual(response.status_code, 404)
        booking = Booking.objects.filter(bookingRef='BB12', passport_number=12345678)
        self.assertFalse(booking.exists())

class cancelBookingViewTest(TestCase):

    def setUp(self):
        # Create a flight and booking for testing
        airline = Airline.objects.create(name='Test Airline', code = 'TT', country = 'United Kingdom', phone = "+44-800-101-111")
        departure_airport = Airport.objects.create(ident='AAA', name='Departure Airport', city = "Manchester", country = 'United Kingdom')
        destination_airport = Airport.objects.create(ident='BBB', name='Destination Airport', city = "Manchester", country = 'United Kingdom')
        self.flight = Flight.objects.create(
            flight_code='TT124',
            departure_date_time=timezone.now(),
            arrival_date_time=timezone.now() + timedelta(hours=2),
            duration_time=timedelta(hours=2),
            base_price=100,
            total_seats=100,
            available_seats=100,
            airline=airline,
            departure_airport=departure_airport,
            destination_airport=destination_airport,
        )
        #Create the booking
        self.booking = Booking.objects.create(
            bookingRef='BB45',
            passport_number='1234',
            flight=self.flight,
        )
        self.booking.refresh_from_db()
        #Initialize the client
        self.client = Client()

    def test_cancel_booking(self):

        #Send a Delete request to the server with the booking reference.
        url = reverse('Bookings')
        response = self.client.delete(f"{url}?booking_ref={self.booking.bookingRef}")
        self.assertEqual(response.status_code, 204)

        #check if the booking got deleted.
        with self.assertRaises(Booking.DoesNotExist):
            Booking.objects.get(bookingRef='BB45')

        #Check that the available seats were updated
        flight = Flight.objects.get(flight_code='TT124')
        self.assertEqual(flight.available_seats, 101)


                