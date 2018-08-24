from django.shortcuts import render, redirect
import aqi
import requests
# Create your views here.
def index(request):
    url = ('http://api.waqi.info/feed/seattle/?token=1efcfae1ada2efa2270689923652087180093867')
    response = requests.get(url)
    air_quality = response.json()
    print (air_quality)
    context = {
        'air_quality': air_quality,
    }
    return render(request, 'air_quality_api/index.html', context)