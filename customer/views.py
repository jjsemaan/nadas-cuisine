from django.shortcuts import render, redirect
from django.views import View
from .models import MenuItem, Category, OrderModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm 

"""
# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the new user immediately after registration
            return redirect('index')  # Redirect to the homepage or another appropriate page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
"""

# Class-based views for authentication
# class HomeView(TemplateView):
#     template_name = 'customer/index.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')

# Class-based views for pages
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class Contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/contact.html')

class Order(LoginRequiredMixin, View):  # Ensure only logged-in users can access this view
    def get(self, request, *args, **kwargs):
        categories = ['Appetiser', 'Plate', 'Dessert', 'Drink']
        context = {category.lower() + 's': MenuItem.objects.filter(category__name__icontains=category) for category in categories}
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(price=price)
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price
        }

        return render(request, 'customer/orderconfirm.html', context)