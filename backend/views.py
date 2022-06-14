from django.shortcuts import render
from .models import Usuario

# Create your views here.

def login(request):
    return render(request, 'login.html')