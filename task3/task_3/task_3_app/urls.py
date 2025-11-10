from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_view, name='base'),
    
    # Passenger URLs
    path('passengers/', views.passenger_list, name='passenger_list'),
    path('passengers/create/', views.passenger_create, name='passenger_create'),
    path('passengers/<int:pk>/edit/', views.passenger_edit, name='passenger_edit'),
    path('passengers/<int:pk>/delete/', views.passenger_delete, name='passenger_delete'),
    
    # Flight URLs
    path('flights/', views.flight_list, name='flight_list'),
    path('flights/create/', views.flight_create, name='flight_create'),
    path('flights/<int:pk>/edit/', views.flight_edit, name='flight_edit'),
    path('flights/<int:pk>/delete/', views.flight_delete, name='flight_delete'),
    
    # Ticket URLs
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/create/', views.ticket_create, name='ticket_create'),
    path('tickets/<int:pk>/edit/', views.ticket_edit, name='ticket_edit'),
    path('tickets/<int:pk>/delete/', views.ticket_delete, name='ticket_delete'),
]