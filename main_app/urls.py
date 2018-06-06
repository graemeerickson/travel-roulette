from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('user/<username>/', views.profile, name='profile'),
  path('login/', views.login_view, name="login"),
  path('logout/', views.logout_view, name="logout"),
  path('destinations/', views.destinations_view, name="destinations"),
]