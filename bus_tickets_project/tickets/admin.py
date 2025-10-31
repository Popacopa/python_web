from django.contrib import admin
from .models import Passenger, Flight, TicketOrder, BusType, Operator, WeekDay

@admin.register(WeekDay)
class WeekDayAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(BusType)
class BusTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity', 'has_ac', 'has_wifi']
    list_filter = ['has_ac', 'has_wifi']
    search_fields = ['name']

@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email']

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'passport_number']
    search_fields = ['name', 'passport_number', 'phone']
    list_filter = ['name']

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['number', 'departure', 'destination', 'bus_type', 'operator', 'departure_time', 'arrival_time']
    list_filter = ['bus_type', 'operator', 'operating_days']
    search_fields = ['number', 'departure', 'destination']
    filter_horizontal = ['operating_days']

@admin.register(TicketOrder)
class TicketOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'passenger', 'flight', 'departure_date', 'seat_number', 'price', 'status']
    list_filter = ['status', 'departure_date', 'flight']
    search_fields = ['passenger__name', 'flight__number']
    readonly_fields = ['order_date']