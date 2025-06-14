# shop/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'description', 'price', 'category']  # ✅ category bor bo‘lishi uchun modelda ham bo‘lishi kerak



