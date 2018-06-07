from django import forms

class LoginForm(forms.Form):
  username = forms.CharField(label="Username", max_length=64)
  password = forms.CharField(widget=forms.PasswordInput())

class SignupForm(forms.Form):
  username = forms.CharField(label="Username", max_length=64)
  password = forms.CharField(widget=forms.PasswordInput())

class DestinationSearchForm(forms.Form):
  trip_purpose = forms.CharField(max_length=100)
  selected_region = forms.CharField(max_length=100)