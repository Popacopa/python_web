from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('create/', views.flight_create, name='flight_create'),
    path('update/<int:pk>/', views.flight_update, name='flight_update'),
    path('delete/<int:pk>/', views.flight_delete, name='flight_delete'),
]