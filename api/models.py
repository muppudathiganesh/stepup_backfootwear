from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, default="Unknown")

    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    style = models.CharField(max_length=100, default='Casual')
    color = models.CharField(max_length=50, default='Black')
    mrp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.00)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)



    def __str__(self):
        return self.name



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
