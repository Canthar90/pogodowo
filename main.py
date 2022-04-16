import requests
import datetime
import json


# lon = 18.0927
# lat = 52.2431
# rain_lon = 13.2
# rain_lat = 47.48
with open("places.json") as file:
    places = json.load(file)

WEATHER_API = "https://api.openweathermap.org/data/2.5/onecall?"


api_key = "key"
for city in places:

    parameters = {
        "lat": places[city][0],
        "lon": places[city][1],
        "exclude": "current,minutely,daily",
        "appid": api_key,
        "units": 'metric',
        "lang": "pl"
    }

    # city

    response = requests.get(WEATHER_API, params=parameters)
    response.raise_for_status()
    weather_data = response.json()

    # print(weather_data)
    # print(weather_data["hourly"][1]["weather"][0]["id"])
    gonna_rain = False
    weather_hourly = weather_data["hourly"]
    weather_future = weather_hourly[:12]
    time = datetime.datetime.now()



    for hour_data in weather_future:
        weather_id = hour_data["weather"][0]["id"]
        if int(weather_id) <700:
            gonna_rain = True


    if gonna_rain:
        print(f"Prognoza pogody dla miasta {city}\n"
              f"Obecna temperatura to: {weather_hourly[0]['temp']}, odczuwalna: {weather_hourly[0]['feels_like']}, "
              f"ciśnienie: {weather_hourly[0]['pressure']}, widoczność: {weather_hourly[0]['visibility']}m, "
              f"prędkość watru: {weather_hourly[0]['wind_speed']}km/h, UWAGA PADA DYSZCZ!!!!!! \n"
              f"Przyszła temperatura to: {weather_hourly[6]['temp']}, odczuwalna: {weather_hourly[6]['feels_like']}, "
              f"ciśnienie: {weather_hourly[6]['pressure']}, widoczność: {weather_hourly[6]['visibility']}m, "
              f"prędkość watru: {weather_hourly[6]['wind_speed']}km/h, {weather_hourly[6]['weather'][0]['description']}")

        # print(f"Przyszła temperatura to: {weather_hourly[6]['temp']}, odczuwalna: {weather_hourly[6]['feels_like']}, "
        #       f"ciśnienie: {weather_hourly[6]['pressure']}, widoczność: {weather_hourly[6]['visibility']}m, "
        #       f"prędkość watru: {weather_hourly[6]['wind_speed']}km/h, {weather_hourly[6]['weather'][0]['description']}")
    else:
        print(f"Prognoza pogody dla miasta {city}\n"
              f"Obecna temperatura to: {weather_hourly[0]['temp']}, odczuwalna: {weather_hourly[0]['feels_like']}, "
                f"ciśnienie: {weather_hourly[0]['pressure']}, widoczność: {weather_hourly[0]['visibility']}m, "
                f"prędkość watru: {weather_hourly[0]['wind_speed']}km/h, Nie pada,"
              f" {weather_hourly[0]['weather'][0]['description']} \n"
              f"Przyszła temperatura to: {weather_hourly[6]['temp']}, odczuwalna: {weather_hourly[6]['feels_like']}, "
              f"ciśnienie: {weather_hourly[6]['pressure']}, widoczność: {weather_hourly[6]['visibility']}m, "
              f"prędkość watru: {weather_hourly[6]['wind_speed']}km/h, Nie pada,"
              f" {weather_hourly[6]['weather'][0]['description']}")
        # print(f"Przyszła temperatura to: {weather_hourly[6]['temp']}, odczuwalna: {weather_hourly[6]['feels_like']}, "
        #       f"ciśnienie: {weather_hourly[6]['pressure']}, widoczność: {weather_hourly[6]['visibility']}m, "
        #       f"prędkość watru: {weather_hourly[6]['wind_speed']}km/h, Nie pada,"
        #       f" {weather_hourly[6]['weather'][0]['description']}")
