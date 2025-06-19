from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    phoneNumber=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES=(
        ('PENDING','Pending'),
        ('SHIPPED','Shipped'),
        ('DELIVERED','Delivered')
    )
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='order')
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='PENDING')
    order_date=models.DateTimeField(auto_now_add=True)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)

    def __str__(self):
        return f"ORDER {self.id} by {self.customer}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_items')
    quantity=models.PositiveIntegerField(default=1)
    unit_price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.quantity} X {self.product.name} in order {self.order.id}"
    