from django.db import models
from shop.models import Product
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Order(models.Model):
    STATUS_CHOICES = [
        ('N', 'New'),
        ('P', 'Processing'),
        ('AP', 'Available for Pick-Up'),
        ('OD', 'Out for Delivery'),
        ('UC', 'Unfulfilled and Closed'),
        ('FC', 'Fulfilled and Closed')
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='N')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)

    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity