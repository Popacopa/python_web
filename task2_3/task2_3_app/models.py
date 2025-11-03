from django.db import models

from django.db import models


class Passenger(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО пассажира")
    phone = models.CharField(max_length=15, blank=True, verbose_name="Телефон")
    email = models.EmailField(blank=True, verbose_name="Email")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пассажир"
        verbose_name_plural = "Пассажиры"


class Flight(models.Model):
    flight_number = models.CharField(max_length=20, verbose_name="Номер рейса")
    departure = models.CharField(max_length=100, verbose_name="Пункт отправления")
    destination = models.CharField(max_length=100, verbose_name="Пункт назначения")
    day_of_week = models.CharField(max_length=15, verbose_name="День недели")
    departure_time = models.TimeField(verbose_name="Время отправления")

    def __str__(self):
        return f"{self.flight_number} ({self.departure} → {self.destination})"

    class Meta:
        verbose_name = "Рейс"
        verbose_name_plural = "Рейсы"


class TicketOrder(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, verbose_name="Пассажир")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name="Рейс")
    seat_number = models.CharField(max_length=5, verbose_name="Номер места")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    order_status = models.CharField(
        max_length=20,
        choices=[
            ('booked', 'Забронирован'),
            ('paid', 'Оплачен'),
            ('cancelled', 'Отменен')
        ],
        default='booked',
        verbose_name="Статус заказа"
    )

    class Meta:
        verbose_name = "Заказ билета"
        verbose_name_plural = "Заказы билетов"
        unique_together = ('flight', 'seat_number')

    def __str__(self):
        return f"{self.passenger} - {self.flight} - Место {self.seat_number}"