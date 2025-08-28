from django.shortcuts import render
from django.contrib import messages
import requests
import datetime
# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST.get('city', 'Nairobi')
    else:
        city = request.GET.get('city', 'Nairobi')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d9f92a94590528dd16e58846485fc9ee'
    PARAMS = {'units':'metric'}
    API_KEY = 'AIzaSyCfFdWSrMiMqYz1b_utlZwFuju8IM0mFxs'
    SEARCH_ENGINE_ID = '8537c912911e5426c'
    query = city + '1920x1080'
    page = 1
    start = (page-1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"
    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']
    try:
        data = requests.get(url,PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()
        return render(request,'weatherapp/index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city,'exception_occured':False,'image_url':image_url})
    except:
        exception_occured = True
        messages.error(request,'entered data is not available to API')
        day = datetime.date.today()
        return render(request,'weatherapp/index.html',{'description':'clear sky','icon':'01d','temp':25,'day':day,'city':'indore','exception_occured':True})
