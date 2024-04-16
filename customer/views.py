from django.shortcuts import render, redirect
from django.views import View
from .models import MenuItem, Category, OrderModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import SignUpForm, UserForm, ProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from customer.models import Profile

from django.views.generic import DeleteView

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        response = super().form_valid(form)
        messages.success(self.request, 'Your account has been created successfully! You can now log in.')
        return response

    def form_invalid(self, form):
        # This method is called if the form is invalid.
        # It should return an HttpResponse.
        response = super().form_invalid(form)
        messages.error(self.request, 'Registration failed. Please correct the errors below.')
        return response

# Class-based views for pages
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')


from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MenuItem, OrderModel  # Adjust the import path based on your project structure

class Order(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        categories = ['Appetiser', 'Plate', 'Dessert', 'Drink']
        context = {
            category.lower() + 's': MenuItem.objects.filter(category__name__icontains=category)
            for category in categories
        }
        context['location'] = request.user.profile.location
        context['phone_number'] = request.user.profile.phone_number
        
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        order_items = {'items': []}
        items = request.POST.getlist('items[]')
        
        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item))
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

        user_id = request.user.id
        delivery_date = request.POST.get('delivery_date')

        order = OrderModel.objects.create(user_id=user_id, price=price, delivery_date=delivery_date)
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price,
            'delivery_date': delivery_date,  # Include delivery_date in the context
            'location': request.user.profile.location,
            'phone_number': request.user.profile.phone_number
        }

        return render(request, 'customer/orderconfirm.html', context)




# View profile and update it
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'customer/profile.html'

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'customer/profile-update.html'

    def post(self, request):

        post_data = request.POST or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class DeleteMenuItem(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a MenuItem"""
    model = MenuItem
    success_url = '/order/'

    def test_func(self):
        return self.request.user.is_superuser
