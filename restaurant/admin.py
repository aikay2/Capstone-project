from django.contrib import admin
from .models import Booking, Menu

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'no_of_guests', 'booking_date']
    list_filter = ['booking_date']
    ordering = ['booking_date']
    
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory']
    ordering = ['price']
    search_fields = ['title']