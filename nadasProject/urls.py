from django.contrib import admin
from django.urls import path, include
from customer.views import (
    Index,
    About,
    Order,
    SignUpView,
    ProfileUpdateView,
    ProfileView,
    DeleteMenuItem,
    CustomLoginView,
)
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Backend
    path("admin/", admin.site.urls),
    # Pages
    path("", Index.as_view(), name="index"),
    path("about/", About.as_view(), name="about"),
    path("order/", Order.as_view(), name="order"),
    # Authentication
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", SignUpView.as_view(), name="register"),
    path("accounts/login/", CustomLoginView.as_view(), name="login"),
    path(
        "accounts/logout/", auth_views.LogoutView.as_view(next_page="/"),
        name="logout"
    ),
    # Change password
    path(
        "change-password/",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/change-password.html", success_url="/"
        ),
        name="change-password",
    ),
    # Profile view and update
    path(
        "profile-update/", ProfileUpdateView.as_view(), name="profile_update"),
    path("profile/", ProfileView.as_view(), name="profile"),
    # Delete menu items
    path(
        "menu-delete-item/<int:pk>/",
        DeleteMenuItem.as_view(), name="delete_menu_item"
    ),
]
