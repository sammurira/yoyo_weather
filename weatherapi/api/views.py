import logging

from django.shortcuts import render
import json
import credentials
import urllib.request
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


@csrf_exempt
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        days = request.POST['days']


        logging.log(2005, "City " + city + "  Days " + days)

        base_url = 'https://api.weatherapi.com/v1/forecast.json?key'
        url = f"{base_url}={credentials.api_key}&q={city}&days={days}"

        logging.log(2005, "url  " + url)

        source = urllib.request.urlopen(url).read()

        weather_data = json.loads(source)

    else:
        weather_data = {}
    return HttpResponse(json.dumps(weather_data), content_type="application/json")
