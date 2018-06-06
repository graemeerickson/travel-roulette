from .forms import LoginForm
from .models import Destination
from datetime import date
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import simplejson as json
import random
import requests

def index(request):
  destinations = Destination.objects.all()
  return render(request, 'index.html', {'destinations': destinations})

def profile(request, username):
  user = User.objects.get(username=username)
  # destinations = Destination.objects.filter(user=user)
  return render(request, 'profile.html', {'username': username})

def login_view(request):
  if request.method == 'POST':
    # if post, then authenticate (user submitted username and password)
    form = LoginForm(request.POST)
    if form.is_valid():
      u = form.cleaned_data['username']
      p = form.cleaned_data['password']
      user = authenticate(username = u, password = p)
      if user is not None:
        if user. is_active:
          login(request, user)
          return HttpResponseRedirect('/')
        else:
          print("The account has been disabled.")
      else:
        print("The username and/or password is incorrect.")
  else:
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/')

def destinations_view(request):
  random_destination_id = random.randint(1,Destination.objects.count())
  random_destination = Destination.objects.get(id=random_destination_id)
  foursquare_version = '20180605'
  foursquare_url = 'https://api.foursquare.com/v2/venues/explore'
  foursquare_params_sights = dict(
    client_id=settings.CLIENT_ID,
    client_secret=settings.CLIENT_SECRET,
    v=foursquare_version,
    near=random_destination.city + ', ' + random_destination.country,
    section='sights',
    locale='en',
    limit=3
  )
  foursquare_params_food = dict(
    client_id=settings.CLIENT_ID,
    client_secret=settings.CLIENT_SECRET,
    v=foursquare_version,
    near=random_destination.city + ', ' + random_destination.country,
    section='food',
    locale='en',
    limit=3
  )
  foursquare_params_drinks = dict(
    client_id=settings.CLIENT_ID,
    client_secret=settings.CLIENT_SECRET,
    v=foursquare_version,
    near=random_destination.city + ', ' + random_destination.country,
    section='drinks',
    locale='en',
    limit=3
  )
  resp_sights = requests.get(url=foursquare_url, params=foursquare_params_sights).json()
  resp_food = requests.get(url=foursquare_url, params=foursquare_params_food).json()
  resp_drinks = requests.get(url=foursquare_url, params=foursquare_params_drinks).json()

  destination = { 'city': random_destination.city, 'country': random_destination.country, 'sights': [], 'food': [], 'drinks': [] }

  for i in range(3):
    destination['sights'].append({
      'sight_name': resp_sights['response']['groups'][0]['items'][i]['venue']['name'],
      'long': resp_sights['response']['groups'][0]['items'][i]['venue']['location']['lng'],
      'lat': resp_sights['response']['groups'][0]['items'][i]['venue']['location']['lat'],
      'address_street': resp_sights['response']['groups'][0]['items'][i]['venue']['location']['address'],
      'address_city': resp_sights['response']['groups'][0]['items'][i]['venue']['location']['city'],
      'address_country': resp_sights['response']['groups'][0]['items'][i]['venue']['location']['country'],
      'address_formatted': resp_sights['response']['groups'][0]['items'][i]['venue']['location']['formattedAddress'],
      'category': resp_sights['response']['groups'][0]['items'][i]['venue']['categories'][0]['name'],
    })
    destination['food'].append({
      'restaurant_name': resp_food['response']['groups'][0]['items'][i]['venue']['name'],
      'long': resp_food['response']['groups'][0]['items'][i]['venue']['location']['lng'],
      'lat': resp_food['response']['groups'][0]['items'][i]['venue']['location']['lat'],
      'address_street': resp_food['response']['groups'][0]['items'][i]['venue']['location']['address'],
      'address_city': resp_food['response']['groups'][0]['items'][i]['venue']['location']['city'],
      'address_country': resp_food['response']['groups'][0]['items'][i]['venue']['location']['country'],
      'address_formatted': resp_food['response']['groups'][0]['items'][i]['venue']['location']['formattedAddress'],
    })
    destination['drinks'].append({
      'bar_name': resp_drinks['response']['groups'][0]['items'][i]['venue']['name'],
      'long': resp_drinks['response']['groups'][0]['items'][i]['venue']['location']['lng'],
      'lat': resp_drinks['response']['groups'][0]['items'][i]['venue']['location']['lat'],
      'address_street': resp_drinks['response']['groups'][0]['items'][i]['venue']['location']['address'],
      'address_city': resp_drinks['response']['groups'][0]['items'][i]['venue']['location']['city'],
      'address_country': resp_drinks['response']['groups'][0]['items'][i]['venue']['location']['country'],
      'address_formatted': resp_drinks['response']['groups'][0]['items'][i]['venue']['location']['formattedAddress'],
    })

  return JsonResponse(destination)

def pretty_request(request):
  headers = ''
  for header, value in request.META.items():
    if not header.startswith('HTTP'):
        continue
    header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
    headers += '{}: {}\n'.format(header, value)

  return (
    '{method} HTTP/1.1\n'
    'Content-Length: {content_length}\n'
    'Content-Type: {content_type}\n'
    '{headers}\n\n'
    '{body}'
  ).format(
    method=request.method,
    content_length=request.META['CONTENT_LENGTH'],
    content_type=request.META['CONTENT_TYPE'],
    headers=headers,
    body=request.body,
  )