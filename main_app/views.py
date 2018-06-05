from django.shortcuts import render

class Destination:
  def __init__(self, city, country, region):
    self.city = city
    self.country = country
    self.region = region

destinations = [
  Destination('Seattle','United States of America','North America'),
  Destination('Barcelona','Spain','Europe'),
  Destination('Tokyo','Japan','Asia')
]

def index(request):
  return render(request, 'index.html', {'destinations': destinations})