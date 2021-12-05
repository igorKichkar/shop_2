from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('products/<str:ct_model>/<str:slug>', ProductDetailViewes.as_view(), name='product_detail')
]
