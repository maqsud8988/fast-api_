from django.urls import path
from .views import ProductView, CategoryView, OrderView
urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('order/', OrderView.as_view(), name='order'),
    path('products/', ProductView.as_view(), name='product'),
]