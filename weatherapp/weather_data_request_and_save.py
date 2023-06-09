import requests

# api-endpoint
URL = "https://api.open-meteo.com/v1/forecast?latitude=50.06&longitude=19.94&hourly=temperature_2m,relativehumidity_2m&current_weather=true"
URL2 = "https://api.open-meteo.com/v1/forecast?latitude=52.23&longitude=21.01&hourly=temperature_2m,relativehumidity_2m&current_weather=true"


r = requests.get(url=URL)
r2 = requests.get(url=URL2)

data = r.json()
data2 = r2.json()
# print(data["current_weather"])
# print(data2["current_weather"])

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weatherapp.settings")
import django
django.setup()

from plots.models import Location, Anemometer, Thermometer, WeatherReport

krakow = Location.objects.get(location_name="Krakow")
warszawa = Location.objects.get(location_name="Warszawa")

t1 = Thermometer(temperature=data["current_weather"]["temperature"])
t1.save()
t2 = Thermometer(temperature=data2["current_weather"]["temperature"])
t2.save()

a1 = Anemometer(wind_speed=data["current_weather"]["windspeed"], wind_direction=data["current_weather"]["winddirection"])
a1.save()
a2 = Anemometer(wind_speed=data2["current_weather"]["windspeed"], wind_direction=data2["current_weather"]["winddirection"])
a2.save()

w1 = WeatherReport(thermometer_measurement=t1, anemometer_measurement=a1, time=data["current_weather"]["time"], location=krakow)
w1.save()
w2 = WeatherReport(thermometer_measurement=t2, anemometer_measurement=a2, time=data2["current_weather"]["time"], location=warszawa)
w2.save()
