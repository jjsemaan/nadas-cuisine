from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def my_customer(request):
    return HttpResponse("Hello, Customer!")