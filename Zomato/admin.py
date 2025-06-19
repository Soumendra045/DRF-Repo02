from django.contrib import admin

# Register your models here.
from .models import Product , Order,Customer,OrderItem

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(OrderItem)