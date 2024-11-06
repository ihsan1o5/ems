from django.contrib import admin
from .models import Client, Vehicle, Shipment, Fuel, FuelExpense


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Client._meta.fields]
    fields = ['name', 'cnic', 'address']

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vehicle._meta.fields]
    fields = ['name', 'vehicle_model', 'number']

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Shipment._meta.fields]
    fields = ['client', 'vehicle', 'load', 'load_unit', 'price', 'paid_amount', 'time_departure', 'is_delivered', 'is_paid']

@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Fuel._meta.fields]
    fields = ['fuel_category', 'quantity', 'unit', 'price', 'earned_date']

@admin.register(FuelExpense)
class FuelExpenseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FuelExpense._meta.fields]
    fields = ['fuel', 'quantity', 'unit', 'price', 'vehicle', 'client', 'expense_date']


