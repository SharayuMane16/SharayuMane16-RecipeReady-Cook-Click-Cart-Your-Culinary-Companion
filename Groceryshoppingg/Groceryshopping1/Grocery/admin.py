from django.contrib import admin
from .models import *

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['name','email','password']

admin.site.register(Product,AdminProduct),

admin.site.register(Category,AdminCategory),

admin.site.register(Customer,AdminCustomer)