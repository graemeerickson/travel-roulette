from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('user/<username>/', views.profile, name='profile'),
  path('login/', views.login_view, name="login"),
]