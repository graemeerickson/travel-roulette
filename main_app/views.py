from .forms import LoginForm
from .models import Destination
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import json
import random

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
  destinations_count = Destination.objects.count()
  random_destination_index = random.randint(1,destinations_count)
  random_destination = Destination.objects.get(id=random_destination_index)
  destination = {'city': random_destination.city, 'country': random_destination.country}
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