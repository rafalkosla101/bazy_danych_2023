from django.db import models


class WeatherReport(models.Model):
    temperature = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.FloatField()
    time = models.DateTimeField()
    location = models.CharField(max_length=250)
