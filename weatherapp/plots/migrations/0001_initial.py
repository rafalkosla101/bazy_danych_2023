# Generated by Django 4.1.3 on 2023-05-13 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('wind_direction', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
