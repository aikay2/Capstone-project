from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from datetime import datetime
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Initialize API client
        self.authenticated_user = User.objects.create_user(username='test', password='test1234')
        self.client = APIClient()
        self.client.login(username='test', password='test1234')
        
        self.unauthenticated_client = APIClient()
        
        # Create test data
        self.item1 = Menu.objects.create(title="Pizza", price=150, inventory=20)
        self.item2 = Menu.objects.create(title="Burger", price=100, inventory=50)
        self.item3 = Menu.objects.create(title="Pasta", price=200, inventory=30)

        # Define URLs
        self.list_url = reverse('menu-list')  # URL for listing Menu items
        self.detail_url = reverse('menu-detail', kwargs={'pk': self.item1.pk})  # URL for detail view of a specific item
    
    def test_getall_authenticated(self):
        response = self.client.get(self.list_url)
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)
        
    def test_getall_unauthenticated(self):
        response = self.unauthenticated_client.get(self.list_url)
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_create_menu_item_authenticated(self):
        data = {'title': 'Pasta', 'price': 200, 'inventory': 30}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 4)  # Check if the new item was created
        self.assertEqual(Menu.objects.latest('id').title, 'Pasta')  # Check the title of the newly created item
    
    def test_create_menu_item_unauthenticated(self):
        data = {'title': 'Pasta', 'price': 200, 'inventory': 30}
        response = self.unauthenticated_client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Menu.objects.count(), 3)  # Check if the new item was created

    def test_retrieve_menu_item_authenticated(self):
        response = self.client.get(self.detail_url)
        serializer = MenuSerializer(self.item1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)
        
    def test_retrieve_menu_item_unauthenticated(self):
        response = self.unauthenticated_client.get(self.detail_url)
        serializer = MenuSerializer(self.item1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_update_menu_item_unauthenticated(self):
        data = {'title': 'Updated Pizza', 'price': 160, 'inventory': 25}
        response = self.unauthenticated_client.put(self.detail_url, data, format='json')
        self.item1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(self.item1.title, 'Pizza')
        self.assertEqual(self.item1.price, 150)
    
    def test_update_menu_item_authenticated(self):
        data = {'title': 'Updated Pizza', 'price': 160, 'inventory': 25}
        response = self.client.put(self.detail_url, data, format='json')
        self.item1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.item1.title, 'Updated Pizza')
        self.assertEqual(self.item1.price, 160)

    def test_delete_menu_item_authenticated(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 2)  # Check if the item was deleted
        
    def test_delete_menu_item_unauthenticated(self):
        response = self.unauthenticated_client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Menu.objects.count(), 3)  # Check if the item was deleted


class BookingViewSetTest(TestCase):
    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username='test', password='test1234')
        self.client = APIClient()
        self.client.login(username='test', password='test1234')
        self.b_date1 = datetime(2024, 8, 15, 14, 30)
        self.b_date2 = datetime(2024, 8, 16, 12, 10)
        
        # Create test data
        self.booking1 = Booking.objects.create(name="John", no_of_guests=5, booking_date=self.b_date1)
        self.booking2 = Booking.objects.create(name="Doe", no_of_guests=3, booking_date=self.b_date2)

        # Define URLs using the router's URL names
        self.list_url = reverse('booking-list')
        self.detail_url = reverse('booking-detail', kwargs={'pk': self.booking1.pk})

    def test_list_bookings(self):
        response = self.client.get(self.list_url)
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_create_booking(self):
        data = {
            'name': "Tom",
            'no_of_guests': 2,
            'booking_date': timezone.make_aware(datetime(2024, 9, 15, 14, 30)).isoformat(),
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 3)  # Check if the new booking was created

    def test_retrieve_booking(self):
        response = self.client.get(self.detail_url)
        serializer = BookingSerializer(self.booking1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_update_booking(self):
        data = {
            'name': "Jonah",
            'no_of_guests': 2,
            'booking_date': timezone.make_aware(datetime(2024, 10, 15, 14, 30)).isoformat(),
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.booking1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.booking1.booking_date, timezone.make_aware(datetime(2024, 10, 15, 14, 30)))

    def test_delete_booking(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 1)  # Check if the booking was deleted