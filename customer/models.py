from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class MenuItem(models.Model):
    # Define the MenuItem model representing items in the menu.
    item_id = models.BigAutoField(primary_key=True)  # Unique identifier for the menu item.
    name = models.CharField(max_length=100)  # Name of the menu item.
    description = models.TextField()  # Description of the menu item.
    price = models.DecimalField(max_digits=5, decimal_places=2)  # Price of the menu item.
    quantity = models.IntegerField(default=1)  # Quantity of the menu item available.
    category = models.ManyToManyField('Category', related_name='item') # models.CharField(max_length=255)  # Category of the menu item.
    image_url = models.URLField(max_length=1024, blank=True, null=True)  # URL of the image

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField(
        'MenuItem', related_name='order', blank=True)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'