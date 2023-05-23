from django.db import models

# Create your models here.

class Seller(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price =models.IntegerField()
    description = models.TextField()
    current_stock = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)
