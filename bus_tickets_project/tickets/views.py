from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Passenger, Flight, TicketOrder, BusType, Operator
from .forms import PassengerForm, FlightForm, TicketOrderForm, BusTypeForm, OperatorForm
from django.contrib import messages
from django.db.models import Q

def index(request):
    stats = {
        'total_passengers': Passenger.objects.count(),
        'total_flights': Flight.objects.count(),
        'total_orders': TicketOrder.objects.count(),
        'recent_orders': TicketOrder.objects.select_related('passenger', 'flight').order_by('-order_date')[:5]
    }
    return render(request, 'tickets/index.html', stats)

# Passenger Views
class PassengerListView(ListView):
    model = Passenger
    template_name = 'tickets/passenger_list.html'
    context_object_name = 'passengers'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(passport_number__icontains=search_query) |
                Q(phone__icontains=search_query)
            )
        return queryset

class PassengerCreateView(CreateView):
    model = Passenger
    form_class = PassengerForm
    template_name = 'tickets/passenger_form.html'
    success_url = reverse_lazy('passenger_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Пассажир успешно создан!')
        return super().form_valid(form)

class PassengerUpdateView(UpdateView):
    model = Passenger
    form_class = PassengerForm
    template_name = 'tickets/passenger_form.html'
    success_url = reverse_lazy('passenger_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Пассажир успешно обновлен!')
        return super().form_valid(form)

class PassengerDeleteView(DeleteView):
    model = Passenger
    template_name = 'tickets/passenger_confirm_delete.html'
    success_url = reverse_lazy('passenger_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Пассажир успешно удален!')
        return super().delete(request, *args, **kwargs)

# Flight Views
class FlightListView(ListView):
    model = Flight
    template_name = 'tickets/flight_list.html'
    context_object_name = 'flights'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset().select_related('bus_type', 'operator')
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(number__icontains=search_query) |
                Q(departure__icontains=search_query) |
                Q(destination__icontains=search_query)
            )
        return queryset
    
class FlightCreateView(CreateView):
    model = Flight
    form_class = FlightForm
    template_name = 'tickets/flight_form.html'
    success_url = reverse_lazy('flight_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Рейс успешно создан!')
        return super().form_valid(form)

class FlightUpdateView(UpdateView):
    model = Flight
    form_class = FlightForm
    template_name = 'tickets/flight_form.html'
    success_url = reverse_lazy('flight_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Рейс успешно обновлен!')
        return super().form_valid(form)

class FlightDeleteView(DeleteView):
    model = Flight
    template_name = 'tickets/flight_confirm_delete.html'
    success_url = reverse_lazy('flight_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Рейс успешно удален!')
        return super().delete(request, *args, **kwargs)

# TicketOrder Views
class TicketOrderListView(ListView):
    model = TicketOrder
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset().select_related('passenger', 'flight', 'operator')
        status_filter = self.request.GET.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset.order_by('-order_date')

class TicketOrderCreateView(CreateView):
    model = TicketOrder
    form_class = TicketOrderForm
    template_name = 'tickets/ticket_form.html'
    success_url = reverse_lazy('ticket_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Заказ билета успешно создан!')
        return super().form_valid(form)

class TicketOrderUpdateView(UpdateView):
    model = TicketOrder
    form_class = TicketOrderForm
    template_name = 'tickets/ticket_form.html'
    success_url = reverse_lazy('ticket_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Заказ билета успешно обновлен!')
        return super().form_valid(form)

class TicketOrderDeleteView(DeleteView):
    model = TicketOrder
    template_name = 'tickets/ticket_confirm_delete.html'
    success_url = reverse_lazy('ticket_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Заказ билета успешно удален!')
        return super().delete(request, *args, **kwargs)

class TicketOrderDetailView(DetailView):
    model = TicketOrder
    template_name = 'tickets/ticket_detail.html'
    context_object_name = 'ticket'

# BusType Views
class BusTypeListView(ListView):
    model = BusType
    template_name = 'tickets/bustype_list.html'
    context_object_name = 'bustypes'

class BusTypeCreateView(CreateView):
    model = BusType
    form_class = BusTypeForm
    template_name = 'tickets/bustype_form.html'
    success_url = reverse_lazy('bustype_list')

class OperatorListView(ListView):
    model = Operator
    template_name = 'tickets/operator_list.html'
    context_object_name = 'operators'

class OperatorCreateView(CreateView):
    model = Operator
    form_class = OperatorForm
    template_name = 'tickets/operator_form.html'
    success_url = reverse_lazy('operator_list')


# BusType Views - дополнительные классы
class BusTypeUpdateView(UpdateView):
    model = BusType
    form_class = BusTypeForm
    template_name = 'tickets/bustype_form.html'
    success_url = reverse_lazy('bustype_list')

class BusTypeDeleteView(DeleteView):
    model = BusType
    template_name = 'tickets/bustype_confirm_delete.html'
    success_url = reverse_lazy('bustype_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Тип автобуса успешно удален!')
        return super().delete(request, *args, **kwargs)

# Operator Views - дополнительные классы
class OperatorUpdateView(UpdateView):
    model = Operator
    form_class = OperatorForm
    template_name = 'tickets/operator_form.html'
    success_url = reverse_lazy('operator_list')

class OperatorDeleteView(DeleteView):
    model = Operator
    template_name = 'tickets/operator_confirm_delete.html'
    success_url = reverse_lazy('operator_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Оператор успешно удален!')
        return super().delete(request, *args, **kwargs)