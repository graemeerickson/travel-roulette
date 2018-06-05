from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
  city = models.CharField(max_length=255)
  country = models.CharField(max_length=255)
  region = models.CharField(max_length=255)

  def __str__(self):
    return self.city