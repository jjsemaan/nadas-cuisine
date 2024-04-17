# Standard library imports
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy

# Local imports
from .models import MenuItem, Category, OrderModel
from .forms import SignUpForm, UserForm, ProfileForm
from customer.models import Profile


class SignUpView(CreateView):
    """
    A view for handling user registration using a custom sign-up form.
    Redirects to the login page upon successful registration.
    """
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        """Saves the form and returns a success message."""
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Your account has been created successfully! You can now log in."
                )
        return response

    def form_invalid(self, form):
        """Returns form errors if the form is invalid."""
        response = super().form_invalid(form)
        messages.error(
            self.request,
            "Registration failed. Please correct the errors below."
                )
        return response


class Index(View):
    """
    A simple view that renders the main index page.
    """
    def get(self, request, *args, **kwargs):
        return render(request, "customer/index.html")


class About(View):
    """
    A view that displays the 'About' page.
    """
    def get(self, request, *args, **kwargs):
        return render(request, "customer/about.html")


class Order(LoginRequiredMixin, View):
    """
    A view for creating orders, displaying menu items sorted by category,
    and managing order submissions.
    """
    def get(self, request, *args, **kwargs):
        categories = ["Appetiser", "Plate", "Dessert", "Drink"]
        context = {
            category.lower() + "s": MenuItem.objects.filter(
                category__name__icontains=category
                )
            for category in categories
        }
        context.update({
            "location": request.user.profile.location,
            "phone_number": request.user.profile.phone_number
        })
        return render(request, "customer/order.html", context)

    def post(self, request, *args, **kwargs):
        items = request.POST.getlist("items[]")
        order_items = {"items": []}
        total_price = 0
        item_ids = []

        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item))
            order_items["items"].append({
                "id": menu_item.pk,
                "name": menu_item.name,
                "price": menu_item.price
            })
            total_price += menu_item.price
            item_ids.append(menu_item.pk)

        order = OrderModel.objects.create(
            user_id=request.user.id,
            price=total_price,
            delivery_date=request.POST.get("delivery_date")
        )
        order.items.add(*item_ids)

        context = {
            "items": order_items["items"],
            "price": total_price,
            **request.POST.dict()
        }
        return render(request, "customer/orderconfirm.html", context)


class ProfileView(LoginRequiredMixin, TemplateView):
    """
    Displays user profile information.
    """
    template_name = "customer/profile.html"


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    """
    Allows users to update their profile information.
    """
    user_form = UserForm
    profile_form = ProfileForm
    template_name = "customer/profile-update.html"

    def post(self, request):
        post_data = request.POST or None
        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile is updated successfully!")
            return HttpResponseRedirect(reverse_lazy("profile"))

        context = self.get_context_data(user_form=user_form, profile_form=profile_form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class DeleteMenuItem(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Provides functionality to delete a menu item.
    Only accessible by users who pass the 'test_func' test (superusers).
    """
    model = MenuItem
    success_url = "/order/"

    def test_func(self):
        return self.request.user.is_superuser


class CustomLoginView(LoginView):
    """
    Customizes the login process by providing specific
    messages on login success or failure.
    """
    template_name = "registration/login.html"
    redirect_authenticated_user = False

    def form_valid(self, form):
        messages.success(self.request, "Login Successful! Welcome back.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Login failed. Check yourusername and password and try again."
        )
        return super().form_invalid(form)
