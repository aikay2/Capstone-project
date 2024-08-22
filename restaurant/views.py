from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import responses
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status, viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
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
    
    @swagger_auto_schema(operation_summary="Retrieve a list of menu items")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Create a new menu item")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    @swagger_auto_schema(operation_summary="Retrieve a specific menu item")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Update a specific menu item")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Delete a specific menu item")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # Include DjangoFilterBackend
    filterset_fields = ['booking_date', 'no_of_guests']
    search_fields = ['name']
    ordering_fields = ['name', 'booking_date']
    
    @swagger_auto_schema(operation_summary="Retrieve a list of bookings")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Create a new booking")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Retrieve a specific booking")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Update a specific booking")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Delete a specific booking")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
