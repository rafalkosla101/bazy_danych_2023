from django.db import models


class Location(models.Model):
    location_name = models.CharField(max_length=250)


class Anemometer(models.Model):
    wind_speed = models.FloatField()
    wind_direction = models.FloatField()


class Thermometer(models.Model):
    temperature = models.FloatField()


class WeatherReport(models.Model):
    thermometer_measurement = models.ForeignKey(Thermometer, on_delete=models.CASCADE, null=True)
    anemometer_measurement = models.ForeignKey(Anemometer, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
