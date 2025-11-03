from django.urls import path
from . import views

app_name = 'task2_3'

urlpatterns = [
    # Главная страница
    path('', views.TicketOrderListView.as_view(), name='home'),
    
    # Passenger URLs
    path('passengers/', views.PassengerListView.as_view(), name='passenger_list'),
    path('passengers/create/', views.PassengerCreateView.as_view(), name='passenger_create'),
    path('passengers/<int:pk>/edit/', views.PassengerUpdateView.as_view(), name='passenger_edit'),
    path('passengers/<int:pk>/delete/', views.PassengerDeleteView.as_view(), name='passenger_delete'),
    
    # Flight URLs
    path('flights/', views.FlightListView.as_view(), name='flight_list'),
    path('flights/create/', views.FlightCreateView.as_view(), name='flight_create'),
    path('flights/<int:pk>/edit/', views.FlightUpdateView.as_view(), name='flight_edit'),
    path('flights/<int:pk>/delete/', views.FlightDeleteView.as_view(), name='flight_delete'),
    
    # TicketOrder URLs
    path('orders/', views.TicketOrderListView.as_view(), name='ticketorder_list'),
    path('orders/create/', views.TicketOrderCreateView.as_view(), name='ticketorder_create'),
    path('orders/<int:pk>/edit/', views.TicketOrderUpdateView.as_view(), name='ticketorder_edit'),
    path('orders/<int:pk>/delete/', views.TicketOrderDeleteView.as_view(), name='ticketorder_delete'),
]