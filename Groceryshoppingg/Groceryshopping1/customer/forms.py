from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import PasswordInput
from  django.utils.translation import gettext,gettext_lazy as _
from .models import Customer1

class Signupform(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm,Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model =User
        fields=['username','email','password1','password2']
        lables={"email":'Email'}
        widgets ={'username':forms.TextInput(attrs={'class':'form-control'})}



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,
                               widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer1
        fields =['name','city','zipcode','state']
        widgets = {'name':forms.TextInput(attrs=
                   {'class':'form-control'}),
                   'city':forms.TextInput(attrs=
                   {'class':'form-control'}),
                   'zipcode':forms.NumberInput(attrs=
                   {'class':'form-control'}),
                   'state': forms.TextInput(attrs=
                  {'class': 'form-control'})}
