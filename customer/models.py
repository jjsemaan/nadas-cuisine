from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import datetime


class Profile(models.Model):
    """
    Extends User model to include additional user information.
    Fields include the user's location and phone number.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create or update the profile whenever a user
    instance is saved. Creates a new profile with the user
    instance if the user is created.
    """
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class MenuItem(models.Model):
    """
    Represents an item on the menu.
    Fields include item ID, name, description, price, quantity,
    category, and optional image URL.
    """
    item_id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=5, decimal_places=2
    )
    quantity = models.IntegerField(default=1)
    category = models.ManyToManyField("Category", related_name="item")
    image_url = models.URLField(
        max_length=1024, blank=True, null=True
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Represents a category for menu items.
    Includes only the category name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OrderModel(models.Model):
    """
    Represents a customer's order, detailing the user,
    date created, total price, items in the order,
    and the delivery date.
    """
    user_id = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField("MenuItem", related_name="order", blank=True)
    delivery_date = models.DateField(
        default=datetime.date.today
    )

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I:%M %p")}'
