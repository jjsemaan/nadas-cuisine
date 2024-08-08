from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from .models import MenuItem, Category, OrderModel
from .forms import SignUpForm, UserForm, ProfileForm
from customer.models import Profile


class SignUpView(CreateView):
    """
    Handles user registration using a custom SignUp form. Upon successful
    registration, redirects to the login page with a success message.
    If registration fails, it displays error messages.
    """
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Your account has been created successfully! You can now log in.",
        )
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(
            self.request, "Registration failed. Correct the errors below."
        )
        return response


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, "customer/index.html")


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, "customer/about.html")


class Order(LoginRequiredMixin, View):
    """
    Manages the display and submission of orders.
    Users can select items categorized by type
    (Appetiser, Plate, Dessert, Drink) and place orders with a delivery date.
    """
    def get(self, request, *args, **kwargs):
        categories = ["Appetiser", "Plate", "Dessert", "Drink"]
        context = {
            category.lower()
            + "s": MenuItem.objects.filter(category__name__icontains=category)
            for category in categories
        }
        context["location"] = request.user.profile.location
        context["phone_number"] = request.user.profile.phone_number

        return render(request, "customer/order.html", context)

    def post(self, request, *args, **kwargs):
        order_items = {"items": []}
        items = request.POST.getlist("items[]")

        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item))
            item_data = {
                "id": menu_item.pk,
                "name": menu_item.name,
                "price": menu_item.price,
            }
            order_items["items"].append(item_data)

        price = 0
        item_ids = []

        for item in order_items["items"]:
            price += item["price"]
            item_ids.append(item["id"])

        user_id = request.user.id
        delivery_date = request.POST.get("delivery_date")

        order = OrderModel.objects.create(
            user_id=user_id, price=price, delivery_date=delivery_date
        )
        order.items.add(*item_ids)

        context = {
            "items": order_items["items"],
            "price": price,
            "delivery_date": delivery_date,
            "location": request.user.profile.location,
            "phone_number": request.user.profile.phone_number,
        }

        return render(request, "customer/orderconfirm.html", context)


class ProfileView(LoginRequiredMixin, TemplateView):
    """
    Displays the user profile page.
    """
    template_name = "customer/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = OrderModel.objects.filter(user_id=self.request.user.id)
        return context


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    """
    Allows users to update their profile information including basic user data
    and profile details.Saves the form data and redirects to the profile page
    on successful update or re-renders the form on errors.
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

        context = self.get_context_data(
            user_form=user_form, profile_form=profile_form
        )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class DeleteMenuItem(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows superuser to delete a menu item.
    Ensures that only users passing the superuser test can perform the action.
    """

    model = MenuItem
    success_url = "/order/"

    def test_func(self):
        return self.request.user.is_superuser


class CustomLoginView(LoginView):
    """
    Customized login view that displays success or error messages based on the
    login attempt's outcome.
    """
    template_name = "registration/login.html"
    redirect_authenticated_user = False

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Login Successful! Welcome back.")
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(
            self.request,
            "Login failed. Check your username and password and try again.",
        )
        return response
