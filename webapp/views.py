from django.shortcuts import render
from django.views import View
from .models import Category, Order, Product


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'category.html', context)


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'product.html', context)


class OrderView(View):
    def get(self, request):
        orders = Order.objects.all()
        context = {
            'orders': orders
        }
        return render(request, 'order.html', context)
