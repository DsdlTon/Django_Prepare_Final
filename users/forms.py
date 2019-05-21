from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm): #create custom auto django's form
    email = forms.EmailField()  #add email field in auto django's register form

    class Meta:
        model = User  #model that you want this form to interect with. In this case this is register user form so it must interect with user model
        fields = ['username', 'email', 'password1', 'password2']   #field that going to be show on the form
