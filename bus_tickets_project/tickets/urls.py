from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
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
    path('tickets/', views.TicketOrderListView.as_view(), name='ticket_list'),
    path('tickets/create/', views.TicketOrderCreateView.as_view(), name='ticket_create'),
    path('tickets/<int:pk>/edit/', views.TicketOrderUpdateView.as_view(), name='ticket_edit'),
    path('tickets/<int:pk>/delete/', views.TicketOrderDeleteView.as_view(), name='ticket_delete'),
    path('tickets/<int:pk>/', views.TicketOrderDetailView.as_view(), name='ticket_detail'),
    
    # BusType URLs
    path('bustypes/', views.BusTypeListView.as_view(), name='bustype_list'),
    path('bustypes/create/', views.BusTypeCreateView.as_view(), name='bustype_create'),
    
    # Operator URLs
    path('operators/', views.OperatorListView.as_view(), name='operator_list'),
    path('operators/create/', views.OperatorCreateView.as_view(), name='operator_create'),

    # BusType URLs
    path('bustypes/<int:pk>/edit/', views.BusTypeUpdateView.as_view(), name='bustype_edit'),
    path('bustypes/<int:pk>/delete/', views.BusTypeDeleteView.as_view(), name='bustype_delete'),

    # Operator URLs
    path('operators/<int:pk>/edit/', views.OperatorUpdateView.as_view(), name='operator_edit'),
    path('operators/<int:pk>/delete/', views.OperatorDeleteView.as_view(), name='operator_delete'),
]