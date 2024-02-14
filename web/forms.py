from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class MyUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'username']


    #for contact 
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
     
     #for website
class WebsiteForm(ModelForm):
    class Meta:
        model = Website
        fields = '__all__'

   