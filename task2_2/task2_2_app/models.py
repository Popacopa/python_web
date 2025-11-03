from django.db import models

# Create your models here.


class BusRaces(models.Model):
    RACES = [
        ("1", "Ярославль - Москва"),
        ("2", "Москва - Ярославль"),
        ("3", "Кострома - Ярославль"),
        ("4", "Ярославль - Кострома"),
        ("5", "Рыбинск - Ярославль"),
        ("6", "Ярославль - Рыбинск"),
    ]
    date = models.DateField()
    time = models.TimeField()
    fromTo = models.CharField( max_length=1, choices=RACES)
    def __str__(self):
        return self.get_fromTo_display()

class Buses(models.Model):
    Busrace = models.ForeignKey(BusRaces, on_delete=models.CASCADE)
    number = models.IntegerField()
    mileAge = models.IntegerField()

    def __str__(self):
        return f'№{str(self.number)}'
