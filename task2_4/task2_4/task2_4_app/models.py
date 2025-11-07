from django.db import models

# Create your models here.


class Driver(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    def __str__(self): return f'{self.first_name} {self.last_name}'


class Route(models.Model):
    city_from = models.CharField(max_length=20, null=False)
    city_to = models.CharField(max_length=20, null=False)
    driver_id = models.OneToOneField(Driver, on_delete=models.CASCADE, primary_key=True)
    def __str__(self): return f'{self.city_from} - {self.city_to}'