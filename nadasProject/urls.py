from django.contrib import admin
from django.urls import path, include
from customer.views import Index, About, Order, Contact
from customer.views import SignUpView
from django.contrib.auth import views as auth_views
from customer.views import ProfileUpdateView, ProfileView, DeleteMenuItem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('order/', Order.as_view(), name='order'),
    path('contact/', Contact.as_view(), name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', SignUpView.as_view(), name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='customer/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html', success_url='/'), name='change-password'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('menu-delete-item/<int:pk>/', DeleteMenuItem.as_view(), name='delete_menu_item'),
]

