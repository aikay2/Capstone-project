from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField()
    
    class Meta:
        ordering = ['booking_date']
    
    def __str__(self):
        return f"{self.name} on {self.booking_date}"
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return f"{self.title} : {str(self.price)}"