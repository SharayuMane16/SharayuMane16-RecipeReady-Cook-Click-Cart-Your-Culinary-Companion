from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse

from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.shortcuts import HttpResponse, render, redirect

from .forms import Signupform, CustomerForm
from .models import Product1
from .models import Category1
from django.contrib import messages


import json
from .models import *


# Create your views here.
def homee(request):
    context = {}
    print('you are:', request.session.get('email'))
    return render(request, 'home.html', context)


class Signup(View):
    def get(self, request):
        form = Signupform()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = Signupform(request.POST)
        if form.is_valid():
            messages.success(request,'Succefullyy signined!!!')
            form.save()
        return render(request, 'signup.html', {'form': form})



class ProfileView(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'profile.html', {'form': form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            zipcode=form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = Customer1(user=usr,name=name,city=city,zipcode=zipcode,state=state )
            reg.save()
        return render(request, 'profile.html', {'form': form, 'active': 'registerbtn'})

def profile(request):
    return render(request, 'profile.html')


def assamfood(request):
    context = {}
    return render(request, 'assamfood.html', context)


def maharashtrian(request):
    context = {}
    return render(request, 'maharashtrian.html', context)


def bengali(request):
    context = {}
    return render(request, 'bengali.html', context)


def bihari(request):
    context = {}
    return render(request, 'bihari.html', context)


class Gujrati(View):

    def post(self, request):
        product1 = request.POST.get('product1')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product1)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product1)
                    else:
                        cart[product1] = quantity - 1
                else:
                    cart[product1] = quantity + 1
            else:
                cart[product1] = 1

        else:
            cart = {}
            cart['products'] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('gujrati')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart['cart'] = {}
        products1 = Product1.objects.filter(id=3)
        context = {'products1': products1}
        return render(request, 'gujrati.html', context)


def gujrati(request):
    context = {}
    return render(request, 'gujrati.html', context)


def punjabi(request):
    context = {}
    return render(request, 'punjabi.html', context)


def kashmir(request):
    context = {}
    return render(request, 'kashmiri.html', context)


def southindian(request):
    context = {}
    return render(request, 'southindian.html', context)


def thalipeeth(request):
    context = {}
    return render(request, 'thalipeeth.html', context)


class Baskets(View):
    def post(self, request):
        product1 = request.POST.get('product1')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product1)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product1)
                    else:
                        cart[product1] = quantity - 1
                else:
                    cart[product1] = quantity + 1
            else:
                cart[product1] = 1
        else:
            cart = {}
            cart['products'] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('baskets')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart['cart'] = {}
        products1 = Product1.objects.filter(category1_id=6)
        context = {'products1': products1}
        return render(request, 'Baskets.html', context)


class Dairys(View):
    def post(self, request):
        product1 = request.POST.get('product1')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product1)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product1)
                    else:
                        cart[product1] = quantity - 1
                else:
                    cart[product1] = quantity + 1
            else:
                cart[product1] = 1
        else:
            cart = {}
            cart['products'] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('dairys')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart['cart'] = {}
        products1 = Product1.objects.filter(category1_id=3)
        context = {'products1': products1}
        return render(request, 'dairy.html', context)

def search(request):
    products1 = Product1.objects.filter(category1_id=6)
    if request.method == 'POST':
        searchh = request.POST.get('searchh')
        products1 = Product1.objects.filter(Q(name__icontains=searchh))
        context = {'products1': products1, }
        return render(request, 'search.html', context)


class Fruitsvegitables(View):
    def post(self, request):
        product1 = request.POST.get('product1')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product1)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product1)
                    else:
                        cart[product1] = quantity - 1
                else:
                    cart[product1] = quantity + 1
            else:
                cart[product1] = 1
        else:
            cart = {}
            cart['products'] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('fruitsvegitables')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart['cart'] = {}
        products1 = Product1.objects.filter(category1_id=2)
        context = {'products1': products1}
        return render(request, 'Vegs.html', context)


def searchveg(request):
    products1 = Product1.objects.filter(category1_id=6)
    if request.method == 'POST':
        searchh = request.POST.get('searchh')

        products1 = Product1.objects.filter(Q(name__icontains=searchh))

        context = {'products1': products1, }
        return render(request, 'searchveg.html', context)



def searchdairy(request):
    products1 = Product1.objects.filter(category1_id=6)
    if request.method == 'POST':
        searchh = request.POST.get('searchh')

        products1 = Product1.objects.filter(Q(name__icontains=searchh))

        context = {'products1': products1, }
        return render(request, 'searchdairy.html', context)


# class Masalas(View):
# def post(self, request):
# product1 = request.POST.get('product1')
#  remove = request.POST.get('remove')
#   cart = request.session.get('cart')
# if cart:
# quantity = cart.get(product1)
# if quantity:
#  if remove:
#  if quantity <= 1:
#    cart.pop(product1)
# else:
#   cart[product1] = quantity - 1
# else:
# cart[product1] = quantity + 1
# else:
# cart[product1] = 1
# else:
# cart = {}
# cart['products'] = 1

# request.session['cart'] = cart
# print(request.session['cart'])
# return redirect('masalas')

# def get(self, request):
# cart = request.session.get('cart')
#  if not cart:
# request.session.cart['cart'] = {}
# products1 = Product1.objects.filter(category1_id=4)
# context = {'products1': products1}
# return render(request, 'masalas.html', context)


def searchmasalas(request):
    products1 = Product1.objects.filter(category1_id=1)
    if request.method == 'POST':
        searchh = request.POST.get('searchh')
        products1 = Product1.objects.filter(Q(name__icontains=searchh))
        context = {'products1': products1, }
        return render(request, 'searchmasala.html', context)

class Productdetail(View):
    def get(self,request,pk):
        product1 = Product1.object.get(pk=pk)
        return render(request,'detail.html',{'product1':product1})


class  Masalas(View):
    def get(self, request):
        products1 = Product1.objects.filter(category1_id=1)
        context = {'products1': products1}
        return render(request, 'masalas.html', context)




def cartt(request):
    user=request.user
    product1 =request.Get.get('product1_id')
    print(product1)
    return render(request,'cart.html')

def masalass(request):

    products1 = Product1.objects.filter(category1_id=1)
    context = {'products1': products1}
    return render(request, 'masalas.html', context)




def cartt(request):
    user=request.user
    product1 =request.Get.get('product1_id')
    print(product1)
    return render(request,'cart.html')


def checkout(request):
    if request.user.is_authenticated:
        customer1 = request.user.customer1
        order1, created = Order1.objects.get_or_create(customer1=customer1, compile=False)
        items = order1.orderitem_set.all()
        cartItems = order1.get_cart_items
    else:
        items = []
        order1 = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order1['get_cart_items']
    context = {'items': items, 'order1': order1}
    return render(request, 'checkout.html', context)



