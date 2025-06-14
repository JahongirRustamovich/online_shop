# shop/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  # ✅ shu yer muhim
    created = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)  # ✅ shu qatorni qo‘shing

    def __str__(self):
        return self.name


