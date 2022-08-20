from django.shortcuts import render
import json
import urllib.request
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        country = request.POST['country']
        api_key = '5d5cc6bbf903febc2a394ec46d69304d'

        source = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q=' + city + ',' + country + '&appid=' + api_key).read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                          + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return HttpResponse(json.dumps(list_of_data), content_type="application/json")
