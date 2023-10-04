from django.contrib.auth.hashers import check_password
from django.shortcuts import HttpResponse, render, redirect



# Create your views here.



def login(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        email = request.POST.get('email')
        password =request.POST.get('password')
        customer = Customer1.get_customer_by_email(email)
        error_message= None
        if customer:
           flag= check_password(password , customer.password)
           if flag:
               return redirect('home.html')
           else:
               error_message = 'Email or Password invalid!!'

        else:
            error_message='Email or Password invalid!!'
        print(customer)
        print(email,password)
        return render(request ,'home.html',{'error' : error_message})

def cart(request):
    context = {}
    return render(request, 'checkout.html', context)

def checkout(request):
    context={}
    return render(request,'checkout.html',context)
def assamfood(request):
    context={}
    return render(request,'assamfood.html',context)
def maharashtrian(request):
    context={}
    return render(request,'maharashtrian.html',context)
def bengali(request):
    context={}
    return render(request,'bengali.html',context)

def bihari(request):
    context={}
    return render(request,'bihari.html',context)

def gujrati(request):
    context={}
    return render(request,'gujrati.html',context)

def kashmiri(request):
    context = {}
    return render(request,'kashmiri.html',context)

def punjabi(request):
    context={}
    return render(request,'punjabi.html',context)

def southindian(request):
    context={}
    return render(request,'southindian.html',context)

def thalipeeth(request):
    context={}
    return render(request,'thalipeeth.html',context)












