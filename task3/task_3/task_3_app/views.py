from django.shortcuts import render, redirect, get_object_or_404
from .models import Passenger, Flight, TicketOrder
from .forms import PassengerForm, FlightForm, TicketOrderForm

def base_view(request):
    return render(request, 'base.html')

# Passenger CRUD
def passenger_list(request):
    passengers = Passenger.objects.all()
    return render(request, 'passenger_list.html', {'passengers': passengers})

def passenger_create(request):
    if request.method == 'POST':
        form = PassengerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('passenger_list')
    else:
        form = PassengerForm()
    return render(request, 'passenger_form.html', {'form': form, 'title': 'Добавить пассажира'})

def passenger_edit(request, pk):
    passenger = get_object_or_404(Passenger, pk=pk)
    if request.method == 'POST':
        form = PassengerForm(request.POST, request.FILES, instance=passenger)
        if form.is_valid():
            form.save()
            return redirect('passenger_list')
    else:
        form = PassengerForm(instance=passenger)
    return render(request, 'passenger_form.html', {'form': form, 'title': 'Редактировать пассажира'})

def passenger_delete(request, pk):
    passenger = get_object_or_404(Passenger, pk=pk)
    if request.method == 'POST':
        passenger.delete()
        return redirect('passenger_list')
    return render(request, 'passenger_confirm_delete.html', {'passenger': passenger})

# Flight CRUD
def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flight_list.html', {'flights': flights})

def flight_create(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm()
    return render(request, 'flight_form.html', {'form': form, 'title': 'Добавить рейс'})

def flight_edit(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm(instance=flight)
    return render(request, 'flight_form.html', {'form': form, 'title': 'Редактировать рейс'})

def flight_delete(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == 'POST':
        flight.delete()
        return redirect('flight_list')
    return render(request, 'flight_confirm_delete.html', {'flight': flight})

# TicketOrder CRUD
def ticket_list(request):
    tickets = TicketOrder.objects.all()
    return render(request, 'ticket_list.html', {'tickets': tickets})

def ticket_create(request):
    if request.method == 'POST':
        form = TicketOrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketOrderForm()
    return render(request, 'ticket_form.html', {'form': form, 'title': 'Создать заказ билета'})

def ticket_edit(request, pk):
    ticket = get_object_or_404(TicketOrder, pk=pk)
    if request.method == 'POST':
        form = TicketOrderForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketOrderForm(instance=ticket)
    return render(request, 'ticket_form.html', {'form': form, 'title': 'Редактировать заказ билета'})

def ticket_delete(request, pk):
    ticket = get_object_or_404(TicketOrder, pk=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket_list')
    return render(request, 'ticket_confirm_delete.html', {'ticket': ticket})