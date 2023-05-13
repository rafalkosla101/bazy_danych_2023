import requests
import sqlite3

# api-endpoint
URL = "https://api.open-meteo.com/v1/forecast?latitude=50.06&longitude=19.94&hourly=temperature_2m,relativehumidity_2m&current_weather=true"
URL2 = "https://api.open-meteo.com/v1/forecast?latitude=52.23&longitude=21.01&hourly=temperature_2m,relativehumidity_2m&current_weather=true"


r = requests.get(url=URL)
r2 = requests.get(url=URL2)

data = r.json()
data2 = r2.json()
print(data["current_weather"])
print(data2["current_weather"])

import sqlite3

try:
    sqliteConnection = sqlite3.connect('D:/bazy_danych_2023/weatherapp/db.sqlite3')
    cursor = sqliteConnection.cursor()

    sqlite_select_Query = """INSERT INTO plots_weatherreport
                                  (temperature, wind_speed, wind_direction, time, location) VALUES (?, ?, ?, ?, ?)"""

    data_tuple = (data["current_weather"]["temperature"], data["current_weather"]["windspeed"],
                  data["current_weather"]["winddirection"], data["current_weather"]["time"], "Krakow")
    print(data_tuple)
    data_tuple2 = (data2["current_weather"]["temperature"], data2["current_weather"]["windspeed"],
                   data2["current_weather"]["winddirection"], data2["current_weather"]["time"], "Warszawa")

    cursor.execute(sqlite_select_Query, data_tuple)
    cursor.execute(sqlite_select_Query,data_tuple2)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")