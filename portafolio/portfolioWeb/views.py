from django.shortcuts import render
from django.http import HttpResponse

# al the def here will be our pages

def home(request):
    
    return HttpResponse(f"Hello, Django!")

# Create your views here.
