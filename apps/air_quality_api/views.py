from django.shortcuts import render, redirect
import aqi
import geopy
from geopy.geocoders import Nominatim
import requests
# Breezyometer api key - 5c3a30fff7ba42749b923c9ef9bd718e
# import pwaqi
# Create your views here.
# def index(request):
#     url = ('http://api.waqi.info/feed/seattle/?token=1efcfae1ada2efa2270689923652087180093867')
#     response = requests.get(url)
#     air_quality = response.json()
#     print (air_quality)
#     context = {
#         'air_quality': air_quality,
#     }
#     return render(request, 'air_quality_api/index.html', context)

def index(request):
    geolocator = Nominatim(user_agent="air_quality_api")
    location = geolocator.geocode("175 5th Avenue NYC")
    print(location.address)
    print((location.latitude, location.longitude))
    lat = location.latitude
    lon = location.longitude
    url = ('https://api.breezometer.com/baqi/?lat=lat&lon=lon&key=5c3a30fff7ba42749b923c9ef9bd718e')
    response = requests.get(url)
    air_quality = response.json()
    print (air_quality)
    context = {
        'air_quality': air_quality,
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
        lat = location.latitude
        lon = location.longitude
        print("Latitude: " + str(lat))
        print("Longitude: " + str(lon))
        # url = ('https://api.breezometer.com/baqi/?lat=lat&lon=lon&key=5c3a30fff7ba42749b923c9ef9bd718e')
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
            'location': location,
        }
        return render(request, 'air_quality_api/result.html', context)