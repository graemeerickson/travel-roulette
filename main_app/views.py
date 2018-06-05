from django.shortcuts import render
from .models import Destination
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

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