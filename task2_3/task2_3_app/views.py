from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Passenger, Flight, TicketOrder

# ========== PASSENGER CRUD ==========
class PassengerListView(ListView):
    model = Passenger
    template_name = 'passenger_list.html'
    context_object_name = 'passengers'

class PassengerCreateView(SuccessMessageMixin, CreateView):
    model = Passenger
    fields = '__all__'
    template_name = 'passenger_form.html'
    success_url = reverse_lazy('task2_3:passenger_list')
    success_message = "Пассажир успешно создан!"

class PassengerUpdateView(SuccessMessageMixin, UpdateView):
    model = Passenger
    fields = '__all__'
    template_name = 'passenger_form.html'
    success_url = reverse_lazy('task2_3:passenger_list')
    success_message = "Пассажир успешно обновлен!"

class PassengerDeleteView(SuccessMessageMixin, DeleteView):
    model = Passenger
    template_name = 'passenger_confirm_delete.html'
    success_url = reverse_lazy('task2_3:passenger_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Пассажир успешно удален!")
        return super().delete(request, *args, **kwargs)

# ========== FLIGHT CRUD ==========
class FlightListView(ListView):
    model = Flight
    template_name = 'flight_list.html'
    context_object_name = 'flights'

class FlightCreateView(SuccessMessageMixin, CreateView):
    model = Flight
    fields = '__all__'
    template_name = 'flight_form.html'
    success_url = reverse_lazy('task2_3:flight_list')
    success_message = "Рейс успешно создан!"

class FlightUpdateView(SuccessMessageMixin, UpdateView):
    model = Flight
    fields = '__all__'
    template_name = 'flight_form.html'
    success_url = reverse_lazy('task2_3:flight_list')
    success_message = "Рейс успешно обновлен!"

class FlightDeleteView(SuccessMessageMixin, DeleteView):
    model = Flight
    template_name = 'flight_confirm_delete.html'
    success_url = reverse_lazy('task2_3:flight_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Рейс успешно удален!")
        return super().delete(request, *args, **kwargs)

# ========== TICKET ORDER CRUD ==========
class TicketOrderListView(ListView):
    model = TicketOrder
    template_name = 'ticketorder_list.html'
    context_object_name = 'orders'

class TicketOrderCreateView(SuccessMessageMixin, CreateView):
    model = TicketOrder
    fields = '__all__'
    template_name = 'ticketorder_form.html'
    success_url = reverse_lazy('task2_3:ticketorder_list')
    success_message = "Заказ билета успешно создан!"

class TicketOrderUpdateView(SuccessMessageMixin, UpdateView):
    model = TicketOrder
    fields = '__all__'
    template_name = 'ticketorder_form.html'
    success_url = reverse_lazy('task2_3:ticketorder_list')
    success_message = "Заказ билета успешно обновлен!"

class TicketOrderDeleteView(SuccessMessageMixin, DeleteView):
    model = TicketOrder
    template_name = 'ticketorder_confirm_delete.html'
    success_url = reverse_lazy('task2_3:ticketorder_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Заказ билета успешно удален!")
        return super().delete(request, *args, **kwargs)