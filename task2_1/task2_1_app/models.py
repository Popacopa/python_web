from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, verbose_name="Номер рейса")
    departure_city = models.CharField(max_length=100, verbose_name="Город отправления")
    arrival_city = models.CharField(max_length=100, verbose_name="Город прибытия")
    departure_date = models.DateField(verbose_name="Дата отправления")
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость билета")
    available_seats = models.IntegerField(verbose_name="Количество свободных мест")

    def __str__(self):
        return f"{self.flight_number} - {self.departure_city} → {self.arrival_city}"

    class Meta:
        verbose_name = "Рейс"
        verbose_name_plural = "Рейсы"
        ordering = ['departure_date']