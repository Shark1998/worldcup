from django.db import models

# Create your models here.
from django.db import models
from PIL import Image

# Create your models here.


class Event(models.Model):
    event_title = models.TextField(max_length=50, verbose_name='Название события')
    date = models.DateField(auto_now_add=False, verbose_name='Дата события', default='01.01.2000')
    teams = models.TextField(max_length=50, verbose_name='Команды участники', default='')
    visitors = models.IntegerField(default=0, verbose_name='Количество зрителей')
    score = models.CharField(max_length=5, verbose_name='Счёт')
    photo = models.TextField(verbose_name='Фото', default='')

    def __str__(self):
        return self.event_title


class Venue(models.Model):
    event = models.ForeignKey(Event, verbose_name='Событие', on_delete=models.CASCADE, default='')
    facility_name = models.TextField(max_length=50, verbose_name='Название сооружения', default='')
    facility_size = models.IntegerField(default=0, verbose_name='Размер сооружения')
    capacity = models.IntegerField(default=0, verbose_name='Вмещаемость')
    photo = models.TextField(verbose_name='Фото', default='')

    def __str__(self):
        return self.facility_name


class Country(models.Model):
    name = models.TextField(max_length=50, verbose_name='Страна', default='')
    city = models.TextField(max_length=50, verbose_name='Город', default='')
    event = models.ForeignKey(Event, verbose_name='Событие', on_delete=models.CASCADE, default='')
    venue = models.ForeignKey(Venue, verbose_name='Сооружение', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name
