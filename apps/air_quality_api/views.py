from django.shortcuts import render, redirect
import aqi
import geopy
from geopy.geocoders import Nominatim
import requests

def forecast(request):
    root_url = 'https://api.breezometer.com/forecast/?lat='
    lat = request.session['lat']
    print("Session Latitude: " + str(lat))
    lon_string = '&lon='
    lon = request.session['lon']
    print("Session Longitude: " + str(lon))
    key_string = '&key=5c3a30fff7ba42749b923c9ef9bd718e'
    url = str(root_url) + str(lat) + str(lon_string) + str(lon) + str(key_string)
    print(url)
    response = requests.get(url)
    forecast = response.json()
    context = {
        'forecast': forecast,
    }
    return render(request, 'air_quality_api/forecast.html', context)

def heatmap(request):
    context = {
    }
    return render(request, 'air_quality_api/heatmap.html', context)

def index(request):
    context = {
    }
    return render(request, 'air_quality_api/index.html', context)


def result(request):
    if request.method == 'POST':
        address = request.POST['address']
        print("Address: " + str(address))
        geolocator = Nominatim(user_agent="air_quality_api")
        location = geolocator.geocode(address)
        print("Location Address: " + str(location))
        print((location.latitude, location.longitude))
        request.session['lat'] = location.latitude
        lat = request.session['lat']
        print("Session Latitude: " + str(lat))
        request.session['lon'] = location.longitude
        lon = request.session['lon']
        print("Session Longitude: " + str(lon))
        # print("Latitude: " + str(lat))
        # print("Longitude: " + str(lon))
        root_url = 'https://api.breezometer.com/baqi/?lat='
        lat = lat
        lon_string = '&lon='
        lon = lon
        key_string = '&key=5c3a30fff7ba42749b923c9ef9bd718e'
        url = str(root_url) + str(lat) + str(lon_string) + str(lon) + str(key_string)
        print(url)
        response = requests.get(url)
        air_quality = response.json()
        print (air_quality)
        context = {
            'address': address,
            'air_quality': air_quality,
            'lat': lat,
            'lon': lon,
            'location': location,
        }
        return render(request, 'air_quality_api/result.html', context)