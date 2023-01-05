from django.shortcuts import render
from django.http import HttpResponse
import re
from django.utils.timezone import datetime

# al the def here will be our pages

def home(request):
    
    title = 'Este es el portafolio de Sheila Álamo'
    
    return render(request,template_name='header.html')

def prueba(request):
    
    return render(template_name='header.html', vars={'message': 'mensaje'})


# Create your views here.
