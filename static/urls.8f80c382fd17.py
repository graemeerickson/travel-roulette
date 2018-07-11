from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('destinations/', views.destinations_view, name="destinations"),
  path('login/', views.login_view, name="login"),
  path('logout/', views.logout_view, name="logout"),
  path('signup/', views.signup_view, name="signup"),
  path('user/<username>/', views.profile, name='profile'),
]