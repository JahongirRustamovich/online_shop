from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})


# Mahsulotlar ro‘yxati
@login_required
def admin_product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/admin/product_list.html', {'products': products})


# Yangi mahsulot qo‘shish
@login_required
def admin_product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductForm()
    return render(request, 'shop/admin/product_form.html', {'form': form})


# Mahsulot tahrirlash
@login_required
def admin_product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/admin/product_form.html', {'form': form})


# Mahsulot o‘chirish
@login_required
def admin_product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('admin_product_list')
    return render(request, 'shop/admin/product_confirm_delete.html', {'product': product})


