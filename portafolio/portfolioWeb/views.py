from django.shortcuts import render
from django.http import HttpResponse
import re
from django.utils.timezone import datetime

# al the def here will be our pages


def home(request):
    # this will be mapped to the home page html to get the sidebar and the menu for the header
    menuSidebar = [
        {'name': 'AboutMe', 'url': '/about-me'},
        {'name': 'Curriculum', 'url': '/curriculum'},
        {'name': 'SketchBook', 'url': '/sketchbook'},
    ]
    return render(request, template_name='header.html')


def AboutMe(request):

    return render(request, 'artwork-section-base.html')


def Curriculum(request):

    return render(request, 'artwork-section-base.html')


def SketchBook(request):

    return render(request, 'artwork-section-base.html')


# Create your views here.
