from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError


class WeekDay(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="Название дня")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "День недели"
        verbose_name_plural = "Дни недели"


class BusType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип автобуса")
    capacity = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Вместимость"
    )
    has_ac = models.BooleanField(default=False, verbose_name="Кондиционер")
    has_wifi = models.BooleanField(default=False, verbose_name="Wi-Fi")
    photo = models.ImageField(upload_to='buses/', blank=True, null=True, verbose_name="Фото")
    
    def __str__(self):
        return f"{self.name} ({self.capacity} мест)"
    
    class Meta:
        verbose_name = "Тип автобуса"
        verbose_name_plural = "Типы автобусов"

class Operator(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя оператора")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    photo = models.ImageField(upload_to='operators/', blank=True, null=True, verbose_name="Фото")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Оператор"
        verbose_name_plural = "Операторы"

class Passenger(models.Model):
    name = models.CharField(
        max_length=100, 
        validators=[MinLengthValidator(2)],
        verbose_name="ФИО пассажира"
    )
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    email = models.EmailField(blank=True, verbose_name="Email")
    passport_number = models.CharField(max_length=20, unique=True, verbose_name="Номер паспорта")
    photo = models.ImageField(upload_to='passengers/', blank=True, null=True, verbose_name="Фото")
    
    def clean(self):
        if not self.phone.isdigit():
            raise ValidationError({'phone': 'Телефон должен содержать только цифры'})
    
    def __str__(self):
        return f"{self.name} ({self.passport_number})"
    
    class Meta:
        verbose_name = "Пассажир"
        verbose_name_plural = "Пассажиры"

class Flight(models.Model):
    number = models.CharField(max_length=10, unique=True, verbose_name="Номер рейса")
    departure = models.CharField(max_length=100, verbose_name="Пункт отправления")
    destination = models.CharField(max_length=100, verbose_name="Пункт назначения")
    bus_type = models.ForeignKey(BusType, on_delete=models.PROTECT, verbose_name="Тип автобуса")
    operator = models.ForeignKey(Operator, on_delete=models.PROTECT, verbose_name="Оператор")
    departure_time = models.TimeField(verbose_name="Время отправления")
    arrival_time = models.TimeField(verbose_name="Время прибытия")
    operating_days = models.ManyToManyField(WeekDay, verbose_name="Дни работы")
    base_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Базовая цена"
    )
    
    def clean(self):
        if self.arrival_time <= self.departure_time:
            raise ValidationError('Время прибытия должно быть после времени отправления')
    
    def __str__(self):
        return f"{self.number}: {self.departure} → {self.destination}"
    
    class Meta:
        verbose_name = "Рейс"
        verbose_name_plural = "Рейсы"

class TicketOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('confirmed', 'Подтвержден'),
        ('cancelled', 'Отменен'),
        ('completed', 'Завершен'),
    ]
    
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, verbose_name="Пассажир")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name="Рейс")
    operator = models.ForeignKey(Operator, on_delete=models.PROTECT, verbose_name="Оператор")
    order_date = models.DateTimeField(default=timezone.now, verbose_name="Дата заказа")
    departure_date = models.DateField(verbose_name="Дата отправления")
    seat_number = models.CharField(max_length=5, verbose_name="Номер места")
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Цена"
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pending',
        verbose_name="Статус"
    )
    notes = models.TextField(blank=True, verbose_name="Примечания")
    
    def clean(self):
        if self.departure_date < timezone.now().date():
            raise ValidationError({'departure_date': 'Дата отправления не может быть в прошлом'})
    
    def __str__(self):
        return f"Билет #{self.id} - {self.passenger.name} на {self.flight}"
    
    class Meta:
        verbose_name = "Заказ билета"
        verbose_name_plural = "Заказы билетов"
        ordering = ['-order_date']