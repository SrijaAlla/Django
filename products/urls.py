from django.urls import path
from django.contrib.auth import views as auth_views

from . import views 
urlpatterns = [
    path('products/', views.product_list, name="product_list"),
    path('products/create/', views.product_create, name="product_create"),
    path('products/<id>/detail/', views.product_detail, name="product_detail"),
    path('products/<id>/update/', views.product_update, name="product_update"),
    path('products/<id>/delete/', views.product_delete, name="product_delete"),
    path('category/', views.category_list, name="category_list")
]