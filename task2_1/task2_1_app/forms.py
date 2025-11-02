from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'
        widgets = {
            'departure_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'flight_number': 'Номер рейса',
            'departure_city': 'Город отправления',
            'arrival_city': 'Город прибытия',
            'departure_date': 'Дата отправления',
            'ticket_price': 'Стоимость билета (руб)',
            'available_seats': 'Свободные места',
        }