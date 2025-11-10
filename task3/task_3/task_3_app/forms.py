# tickets/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Passenger, Bus, Operator, Flight, TicketOrder

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['name', 'passport_number', 'phone', 'email', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'passport_number': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_passport_number(self):
        passport_number = self.cleaned_data['passport_number']
        if not passport_number.replace(' ', '').isalnum():
            raise ValidationError('Номер паспорта должен содержать только буквы и цифры')
        return passport_number

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['number', 'day_of_week', 'departure_time', 'arrival_time', 
                 'departure_city', 'arrival_city', 'bus', 'operator', 'price']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'day_of_week': forms.Select(attrs={'class': 'form-control'}),
            'departure_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'arrival_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'departure_city': forms.TextInput(attrs={'class': 'form-control'}),
            'arrival_city': forms.TextInput(attrs={'class': 'form-control'}),
            'bus': forms.Select(attrs={'class': 'form-control'}),
            'operator': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        departure_time = cleaned_data.get('departure_time')
        arrival_time = cleaned_data.get('arrival_time')
        
        if departure_time and arrival_time and arrival_time <= departure_time:
            raise ValidationError('Время прибытия должно быть позже времени отправления')
        
        return cleaned_data

class TicketOrderForm(forms.ModelForm):
    class Meta:
        model = TicketOrder
        fields = ['passenger', 'flight', 'seat_number', 'ticket_file', 'is_paid']
        widgets = {
            'passenger': forms.Select(attrs={'class': 'form-control'}),
            'flight': forms.Select(attrs={'class': 'form-control'}),
            'seat_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'ticket_file': forms.FileInput(attrs={'class': 'form-control'}),
            'is_paid': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        flight = cleaned_data.get('flight')
        seat_number = cleaned_data.get('seat_number')
        
        if flight and seat_number:
            # Проверка, что номер места не превышает вместимость автобуса
            if seat_number > flight.bus.capacity:
                raise ValidationError(
                    {'seat_number': f'В автобусе всего {flight.bus.capacity} мест'}
                )
            
            # Проверка, что место не занято на этом рейсе
            existing_ticket = TicketOrder.objects.filter(
                flight=flight, 
                seat_number=seat_number
            )
            if self.instance.pk:
                existing_ticket = existing_ticket.exclude(pk=self.instance.pk)
                
            if existing_ticket.exists():
                raise ValidationError(
                    {'seat_number': 'Это место уже занято на данном рейсе'}
                )
        
        return cleaned_data