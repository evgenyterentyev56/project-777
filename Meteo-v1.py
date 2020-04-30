
# Предсказатель погоды =)

import pyowm

owm = pyowm.OWM('b31afd9ac5cd8a470b28960cff1fb12c', language = "ru")  # You MUST provide a valid API key

place = input("В каком городе/стране?: ")

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]


print("В городе " + place + " Сейчас " + w.get_detailed_status())
print("температура сейчас в районе " + str(temp))

if temp < 10:
    print("Сейчас холодно, пиздец!, одевайся норм ")

elif temp < 20:
    print("Сейчас холодно, ОХУЕТЬ КАК!, одевайся СУПЕР! ")

else:
    print("Температура норм, одевай че хошь, ебать :)")