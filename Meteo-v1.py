
# Предсказатель погоды =)

import pyowm

owm = pyowm.OWM('b31afd9ac5cd8a470b28960cff1fb12c', language = "ru")  # You MUST provide a valid API key

place = input("В каком городе/стране?: ")

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place(place)
w = observation.get_weather()
print(w)