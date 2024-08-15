from django.test import TestCase
from datetime import datetime
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        
        self.assertEqual(str(item), "IceCream : 80")
        

class BookingTest(TestCase):
    def test_get_booking(self):
        self.booking_date = datetime(2024, 8, 15, 14, 30)
        booking = Booking.objects.create(name="John", no_of_guests=5, booking_date=self.booking_date)
        
        self.assertEqual(str(booking), f"John on {self.booking_date}")