from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    count = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return f"{self.name} {self.description} {self.count} {self.category} {self.price}"


class OrderStatus(models.TextChoices):
    PENDING = 'PENDING', 'pending'
    TRANSIT = 'TRANSIT', 'transit'
    DELIVERED = 'DELIVERED', 'delivered'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    order_status = models.CharField(max_length=15, choices=OrderStatus.choices, default=OrderStatus.PENDING, )
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f"{self.count} {self.order_status}"