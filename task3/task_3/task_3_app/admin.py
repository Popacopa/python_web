from django.contrib import admin
from .models import Passenger, Bus, Operator, Flight, TicketOrder

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['name', 'passport_number', 'phone', 'email']
    search_fields = ['name', 'passport_number']

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ['model', 'type', 'license_plate', 'capacity']
    list_filter = ['type']

@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'hire_date']

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['number', 'departure_city', 'arrival_city', 'day_of_week', 'departure_time', 'price']
    list_filter = ['day_of_week', 'bus__type']

@admin.register(TicketOrder)
class TicketOrderAdmin(admin.ModelAdmin):
    list_display = ['passenger', 'flight', 'order_date', 'seat_number', 'is_paid']
    list_filter = ['is_paid', 'order_date']