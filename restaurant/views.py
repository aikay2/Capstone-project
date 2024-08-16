from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import responses
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status, viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from.serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking

# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # Include DjangoFilterBackend
    filterset_fields = ['price', 'inventory']
    ordering_fields = ['title', 'price', 'inventory']
    search_fields = ['title']


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # Include DjangoFilterBackend
    filterset_fields = ['booking_date', 'no_of_guests']
    search_fields = ['name']
    ordering_fields = ['name', 'booking_date']
    
