from django.shortcuts import render
from plots.models import WeatherReport, Thermometer, Anemometer, Location
from plots.services import get_min_max_values

# Create your views here.


def weather_data_panel(request, location="krakow"):
    weather_data = WeatherReport.objects.select_related("thermometer_measurement", "anemometer_measurement", "location").filter(location__location_name=location.capitalize())
    temperatures = [wd.thermometer_measurement for wd in weather_data]
    anemometers = [wd.anemometer_measurement for wd in weather_data]

    min_temperature, max_temperature = get_min_max_values(Thermometer.objects.filter(weatherreport__in=weather_data).all(), "temperature")
    min_wind_speed, max_wind_speed = get_min_max_values(Anemometer.objects.filter(weatherreport__in=weather_data).all(), "wind_speed")
    min_wind_direction, max_wind_direction = get_min_max_values(Anemometer.objects.filter(weatherreport__in=weather_data).all(), "wind_direction")

    if request.method == "POST":
        temp_min, temp_max = float(request.POST.get("temp_min")), float(request.POST.get("temp_max"))
        wind_speed_min, wind_speed_max = float(request.POST.get("wind_speed_min")), float(request.POST.get("wind_speed_max"))
        wind_dir_min, wind_dir_max = float(request.POST.get("wind_dir_min")), float(request.POST.get("wind_dir_max"))
        weather_data = WeatherReport.objects.select_related("thermometer_measurement", "anemometer_measurement",
                                                            "location").filter(
            location__location_name=location.capitalize(), thermometer_measurement__temperature__gte=min(temp_min, temp_max),
            thermometer_measurement__temperature__lte=max(temp_min, temp_max), anemometer_measurement__wind_speed__gte=min(wind_speed_min, wind_speed_max),
            anemometer_measurement__wind_speed__lte=max(wind_speed_min, wind_speed_max), anemometer_measurement__wind_direction__gte=min(wind_dir_min, wind_dir_max),
            anemometer_measurement__wind_direction__lte=max(wind_dir_min, wind_dir_max)
        )

        temperatures = [wd.thermometer_measurement for wd in weather_data]
        anemometers = [wd.anemometer_measurement for wd in weather_data]
    context = {
        "temperature": [data.temperature for data in temperatures],
        "wind_speed": [data.wind_speed for data in anemometers],
        "wind_direction": [data.wind_direction for data in anemometers],
        "date": [date["time"] for date in weather_data.values("time")],
        "min_temperature": min_temperature,
        "max_temperature": max_temperature,
        "min_wind_speed": min_wind_speed,
        "max_wind_speed": max_wind_speed,
        "min_wind_direction": min_wind_direction,
        "max_wind_direction": max_wind_direction
    }
    return render(request, 'weather_data_panel.html', context=context)
