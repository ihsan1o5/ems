from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=255)
    cnic = models.BigIntegerField()
    address = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    vehicle_model = models.CharField(max_length=100)
    number = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name + ' ' + self.vehicle_model

class Shipment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    load = models.FloatField(default=0.00)
    load_unit = models.CharField(max_length=30)
    price = models.FloatField(null=True, blank=True, default=0.00)
    paid_amount = models.FloatField(null=True, blank=True, default=0.00)
    time_departure = models.DateTimeField()
    is_delivered = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.client.name + ' ' + self.vehicle.name
    
    @property
    def balance(self):
        """ Calculate Balance """
        if self.price > self.paid_amount:
            return (self.price or 0) - (self.paid_amount or 0)
        else:
            return 0
        
    @classmethod
    def total_price(cls, queryset=None):
        """Calculate the total price for a given queryset, or all instances if none is provided."""
        queryset = queryset if queryset is not None else cls.objects.all()
        return queryset.aggregate(total_price=models.Sum('price'))['total_price'] or 0

    @classmethod
    def total_paid_amount(cls, queryset=None):
        """Calculate the total paid amount for a given queryset, or all instances if none is provided."""
        queryset = queryset if queryset is not None else cls.objects.all()
        return queryset.aggregate(total_paid_amount=models.Sum('paid_amount'))['total_paid_amount'] or 0
    
class Fuel(models.Model):
    fuel_category = models.CharField(max_length=100)
    quantity = models.FloatField(default=0.00)
    unit = models.CharField(max_length=50)
    price = models.FloatField(default=0.00)
    earned_date = models.DateTimeField()

    def __str__(self):
        return self.fuel_category + ' ' + str(self.quantity)

class FuelExpense(models.Model):
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.00)
    unit = models.CharField(max_length=50)
    price = models.FloatField(default=0.00)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    expense_date = models.DateTimeField()

    def __str__(self):
        return self.fuel.fuel_category +' '+ str(self.quantity) +' '+ self.vehicle.name


