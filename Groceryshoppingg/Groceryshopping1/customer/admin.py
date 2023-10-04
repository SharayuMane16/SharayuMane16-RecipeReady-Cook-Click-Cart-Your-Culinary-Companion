from django.contrib import  admin
from  .models import (
Customer1,
Product1,
Category1,
Cart,
Order1Placed
)

@admin.register(Customer1)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','city','zipcode','state']

@admin.register(Product1)
class Product1ModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','category1','description']

@admin.register(Category1)
class Category1ModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product1','quantity']


@admin.register(Order1Placed)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer1','product1', 'date_ordered','transaction_id']

