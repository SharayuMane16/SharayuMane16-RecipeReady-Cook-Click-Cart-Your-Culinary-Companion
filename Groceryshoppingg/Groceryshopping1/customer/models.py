from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer1(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode =models.IntegerField()
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Category1(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
         return self.name

class Product1(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    category1 =models.ForeignKey(Category1,on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    product1 = models.ForeignKey(Product1,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def _str_(self):
        return str(self.id)

class Order1Placed(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    customer1 = models.ForeignKey(Customer1, on_delete=models.SET_NULL, blank=True, null=True)
    product1 =models.ForeignKey(Product1,on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=200, null=True)





