from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login', views.login, name='login'),
    path('cart/', views.cart, name='cart'),



    path('checkout/', views.checkout, name='checkout'),
    path('assamfood/', views.assamfood, name='assamfood'),
    path('maharashtrian/', views.maharashtrian, name='maharashtrian'),
    path('bengali/', views.bengali, name='bengali'),
    path('bihari/', views.bihari, name='bihari'),
    path('gujrati/', views.gujrati, name='gujrati'),
    path('kashmiri/', views.kashmiri, name='kashmiri'),
    path('punjabi/', views.punjabi, name='punjabi'),
    path('southindian/', views.southindian, name='southindian'),
    path('maharashtrian/thalipeeth', views.thalipeeth, name='thalipeeth'),
]