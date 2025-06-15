from django.urls import path
from . import views
from .views import product_list
from .views import ProductListAPIView


urlpatterns = [
    path('', views.index, name='home'),

    # admin viewlar
    path('admin/products/', views.admin_product_list, name='admin_product_list'),
    path('admin/products/create/', views.admin_product_create, name='admin_product_create'),
    path('admin/products/<int:pk>/edit/', views.admin_product_update, name='admin_product_update'),
    path('admin/products/<int:pk>/delete/', views.admin_product_delete, name='admin_product_delete'),
    path('api/products/', product_list, name='product-list'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),

]




