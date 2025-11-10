from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Passenger(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    passport_number = models.CharField(max_length=20, unique=True, verbose_name='Номер паспорта')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email', blank=True)
    photo = models.ImageField(upload_to='passengers/', blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пассажир'
        verbose_name_plural = 'Пассажиры'

class Bus(models.Model):
    BUS_TYPES = [
        ('standard', 'Стандарт'),
        ('comfort', 'Комфорт'),
        ('luxury', 'Люкс'),
    ]
    model = models.CharField(max_length=50, verbose_name='Модель')
    type = models.CharField(max_length=20, choices=BUS_TYPES, verbose_name='Тип')
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(100)],
        verbose_name='Вместимость'
    )
    license_plate = models.CharField(max_length=10, unique=True, verbose_name='Госномер')
    photo = models.ImageField(upload_to='buses/', blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return f"{self.model} ({self.license_plate})"

    class Meta:
        verbose_name = 'Автобус'
        verbose_name_plural = 'Автобусы'

class Operator(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    hire_date = models.DateField(verbose_name='Дата найма')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Оператор'
        verbose_name_plural = 'Операторы'

class Flight(models.Model):
    DAYS_OF_WEEK = [
        ('mon', 'Понедельник'),
        ('tue', 'Вторник'),
        ('wed', 'Среда'),
        ('thu', 'Четверг'),
        ('fri', 'Пятница'),
        ('sat', 'Суббота'),
        ('sun', 'Воскресенье'),
    ]
    number = models.CharField(max_length=10, verbose_name='Номер рейса')
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_WEEK, verbose_name='День недели')
    departure_time = models.TimeField(verbose_name='Время отправления')
    arrival_time = models.TimeField(verbose_name='Время прибытия')
    departure_city = models.CharField(max_length=50, verbose_name='Город отправления')
    arrival_city = models.CharField(max_length=50, verbose_name='Город прибытия')
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, verbose_name='Автобус')
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, verbose_name='Оператор')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена билета')

    def __str__(self):
        return f"Рейс {self.number} ({self.departure_city} - {self.arrival_city})"

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'

class TicketOrder(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, verbose_name='Пассажир')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name='Рейс')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    seat_number = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        verbose_name='Номер места'
    )
    ticket_file = models.FileField(upload_to='tickets/', blank=True, null=True, verbose_name='Файл билета')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')

    def __str__(self):
        return f"Билет {self.passenger} на {self.flight}"

    class Meta:
        verbose_name = 'Заказ билета'
        verbose_name_plural = 'Заказы билетов'
        unique_together = ['flight', 'seat_number']