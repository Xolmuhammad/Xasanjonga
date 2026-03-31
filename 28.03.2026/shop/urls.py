from django.urls import path

from .views import index, product_by_category, product_detail

urlpatterns = [
    path('', index, name='index'),
    path('category/<slug:category_slug>/', product_by_category, name='by_category'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
]
