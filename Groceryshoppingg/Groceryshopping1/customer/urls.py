import profile

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm
from .views import homee,  checkout, search, assamfood, Baskets, maharashtrian, kashmir, bihari, \
    bengali, southindian, punjabi, gujrati, Dairys, Fruitsvegitables, searchmasalas, searchdairy, searchveg, \
    masalass, cartt

urlpatterns=[

    path('',homee,name='homee'),
    path('signup/',views.Signup.as_view(),name='signup'),
    path('login',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='homee'),name='logout'),
    path('cartt/',views.cartt,name='cartt'),
    path('checkout',checkout),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('assamfood',assamfood),
    path('maharashtrian',maharashtrian),
    path('southindian',southindian),
    path('bengali',bengali),
    path('bihari',bihari),
    path('gujrati',gujrati),
    path('baskets',Baskets.as_view(),name='baskets'),
   # path('masalas',Masalas.as_view(),name='masalas'),
    path('dairys', Dairys.as_view(), name='dairys'),
    path('fruitsvegitables', Fruitsvegitables.as_view(), name='fruitsvegitables'),
    path('kashmir',kashmir),
    path('punjabi', punjabi),
    path('search',search),
    path('searchmasalas',searchmasalas),
    path('searchveg',searchveg),
    path('searchdairy',searchdairy),
    path('masalass',masalass),












]