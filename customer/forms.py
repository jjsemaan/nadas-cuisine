from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from customer.models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    phone_number = forms.CharField(max_length=15, required=False)
    location = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user.profile.phone_number = self.cleaned_data['phone_number']
            user.profile.location = self.cleaned_data['location']
            user.profile.save()
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'phone_number',
            'location',
        ]
