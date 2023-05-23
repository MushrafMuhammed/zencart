from django.db import models

from seller.models import Product

# Create your models here.

class Customer(models.Model) :
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=8)

class Cart(models.Model) :
    product_details = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer =models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField()
    phone = models.CharField()
    address = models.CharField()
    place = models.CharField()
    pincode = models.IntegerField()
    email = models.EmailField()
    ordered_date = models.DateTimeField(auto_now_add=True)

    def calculate_grand_total(self):
        return self.cart.quantity * self.cart.price

