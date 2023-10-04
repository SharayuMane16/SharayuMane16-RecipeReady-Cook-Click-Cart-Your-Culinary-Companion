from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    username =models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=500)

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False








    def isExists(self):
       if Customer.objects.filter(email =self.email):
           return True



class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
         return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(max_length=50)
    category =models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=50, default='')