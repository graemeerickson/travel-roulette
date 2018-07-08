from django.db import models

class Destination(models.Model):
  city = models.CharField(max_length=255)
  country = models.CharField(max_length=255)
  region = models.CharField(max_length=255)
  adventure = models.BooleanField(default=False)
  ski = models.BooleanField(default=False)
  beach = models.BooleanField(default=False)
  jan = models.CharField(max_length=10, default='NONE')
  feb = models.CharField(max_length=10, default='NONE')
  mar = models.CharField(max_length=10, default='NONE')
  apr = models.CharField(max_length=10, default='NONE')
  may = models.CharField(max_length=10, default='NONE')
  jun = models.CharField(max_length=10, default='NONE')
  jul = models.CharField(max_length=10, default='NONE')
  aug = models.CharField(max_length=10, default='NONE')
  sep = models.CharField(max_length=10, default='NONE')
  oct = models.CharField(max_length=10, default='NONE')
  nov = models.CharField(max_length=10, default='NONE')
  dec = models.CharField(max_length=10, default='NONE')
  lat = models.DecimalField(max_digits=9, decimal_places=6, default=000.000000)
  long = models.DecimalField(max_digits=9, decimal_places=6, default=000.000000)

  def __str__(self):
    return self.city