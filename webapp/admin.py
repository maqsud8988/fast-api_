from django.contrib import admin
from .models import Order, Product, Category

admin.site.register([Order, Product, Category])
