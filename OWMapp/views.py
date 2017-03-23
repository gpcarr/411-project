from django.shortcuts import render, HttpResponse
from django.template import loader
import requests
import json
import pyowm 

# Create your views here.

def index(request):
    return HttpResponse("Welcome to the Weather site!")

def weather(request):
    #template = loader.get_template('templates_app\weather.html')
    
    owm = pyowm.OWM('c646db9215792630a0891c27e40c6745')
    
    if request.method == 'POST':
        
        city = request.POST.get('city')
        forecast = owm.weather_at_place(city)
        w = forecast.get_weather()
        status = w.get_status()
        
    return render(status, 'OWMapp/weather.html')