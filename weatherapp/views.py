import requests
from django.shortcuts import render

# https://openweathermap.org/current

# Create your views here.
def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=16bf90bbd430c04c1c92dc887d8ccdcc"
    city = 'Tokyo'

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperture': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    context = {'city_weather' : city_weather}

    print(city_weather) # {'city': 'Tokyo', 'temperture': 12.84, 'description': 'broken clouds', 'icon': '04d'}
    return render(request, 'test.html', context)