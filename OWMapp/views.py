from django.shortcuts import render, HttpResponse
from django.template import loader
import requests
import json
import pyowm 
from OWMapp.forms import WeatherForm

# Create your views here.
# reference: http://drksephy.github.io/2015/07/16/django/

def index(request):
    return HttpResponse("Welcome to the Weather site!")

def weather(request):
    #template = loader.get_template('templates_app\weather.html')
    
    parsedData = []
    
    owm = pyowm.OWM('c646db9215792630a0891c27e40c6745')
    
    if request.method == 'POST':

        city = request.POST.get('search-term')
        
        cityData = {}  
        
        forecast = owm.weather_at_place(city)
        w = forecast.get_weather()
        status = w.get_status()
        humidity = w.get_humidity()  
        temperature = w.get_temperature()
        wind = w.get_wind()

        temp = round((((temperature['temp'] - 273.15) * 9 / 5) + 32), 0)
        wind_speed = wind['speed']
        
        cityData['status'] = status
        cityData['humidity'] = humidity
        cityData['temperature'] = temp
        cityData['wind_speed'] = wind_speed
        
        parsedData.append(cityData)
        print(parsedData)
        
    return render(request, 'weather.html', {'data': parsedData})
    