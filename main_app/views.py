from django.shortcuts import render
from .models import Destination
from django.contrib.auth.models import User

def index(request):
  destinations = Destination.objects.all()
  return render(request, 'index.html', {'destinations': destinations})

def profile(request, username):
  user = User.objects.get(username=username)
  # destinations = Destination.objects.filter(user=user)
  return render(request, 'profile.html', {'username': username})