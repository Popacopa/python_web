from django import forms
from .models import Passenger, Flight, TicketOrder, BusType, Operator, WeekDay
from django.core.exceptions import ValidationError
import re

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['name', 'phone', 'email', 'passport_number', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'passport_number': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'ФИО пассажира',
            'phone': 'Телефон',
            'email': 'Email',
            'passport_number': 'Номер паспорта',
            'photo': 'Фото',
        }
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.match(r'^\+?[0-9]{10,15}$', phone):
            raise ValidationError('Введите корректный номер телефона')
        return phone

class BusTypeForm(forms.ModelForm):
    class Meta:
        model = BusType
        fields = ['name', 'capacity', 'has_ac', 'has_wifi', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'has_ac': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_wifi': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = ['name', 'email', 'phone', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

class FlightForm(forms.ModelForm):
    operating_days = forms.ModelMultipleChoiceField(
        queryset=WeekDay.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        label='Дни работы'
    )
    
    class Meta:
        model = Flight
        fields = [
            'number', 'departure', 'destination', 'bus_type', 'operator',
            'departure_time', 'arrival_time', 'operating_days', 'base_price'
        ]
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'departure': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'bus_type': forms.Select(attrs={'class': 'form-control'}),
            'operator': forms.Select(attrs={'class': 'form-control'}),
            'departure_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'arrival_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'base_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class TicketOrderForm(forms.ModelForm):
    class Meta:
        model = TicketOrder
        fields = [
            'passenger', 'flight', 'operator', 'departure_date', 
            'seat_number', 'price', 'status', 'notes'
        ]
        widgets = {
            'passenger': forms.Select(attrs={'class': 'form-control'}),
            'flight': forms.Select(attrs={'class': 'form-control'}),
            'operator': forms.Select(attrs={'class': 'form-control'}),
            'departure_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'seat_number': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }