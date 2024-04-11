from django.contrib import admin
from django.contrib.auth.models import User
from .models import MenuItem, Category, OrderModel, Profile

admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderModel)
admin.site.register(Profile)



