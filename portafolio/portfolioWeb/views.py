from django.shortcuts import render
from django.http import HttpResponse
import re
from django.utils.timezone import datetime

# al the def here will be our pages


def home(request):
    context = {
        'aboutMeText': 'Mi nombre es Sheila Álamo, bienvenidos/as a mi portafolio web, aquí encontrarás mis trabajos más recientes. Soy una persona altamente creativa y con mucha energía, aunque a veces puedo ser algo tímida. Me gradué como técnico de imagen especializado en la ilustración en la EADSGC, más tarde hice los siguientes cursos en la SPEGC: “Diseño UI/UX”, ”Programación Full-Stack”,”Especialización en ML” ',
        'socials': [
            {
                'icons/instagram-logo.svg',
                'https://www.instagram.com/sheila_ilustraciones', 
            },
            {
                'icons/artstation-logo.svg',
                'https://www.artstation.com/sheila-alamo-ilustraciones',
            },
            {
                'icons/linkedin-logo.svg',
                'https://www.linkedin.com/in/sheila-%C3%A1lamo-alarc%C3%B3n-ilustraciones/',
            },
        ],
        'menu': [
            {
                'Curriculum',
                '/curriculum',
            },
            {
                '/sketchbook', 
                'SketchBook',
            },
            {
                '/animations', 
                'Animations',
            },
        ],
        
        'artwork': [
            {
                'https://hayile.netlify.app/',
                'Hayile',
                'artwork-images/hayile/hayile-second-small-image.png',
                'artwork-images/hayile/hayile-big-image.png',
                'artwork-images/hayile/hayile-small-image.png'
            },
        ],
    }
    return render(request, 'header.html', context)


def AboutMe(request):

    return render(request, 'sketchbook.html')


def Curriculum(request):

    return render(request, 'sketchbook.html')


def SketchBook(request):
    
    context = {
        'socials': [
            {
                'icons/instagram-logo.svg',
                'https://www.instagram.com/sheila_ilustraciones', 
            },
            {
                'icons/artstation-logo.svg',
                'https://www.artstation.com/sheila-alamo-ilustraciones',
            },
            {
                'icons/linkedin-logo.svg',
                'https://www.linkedin.com/in/sheila-%C3%A1lamo-alarc%C3%B3n-ilustraciones/',
            },
        ],
        'menu': [
            {
                'Curriculum',
                '/curriculum',
            },
            {
                '/sketchbook', 
                'SketchBook',
            },
            {
                '/animations', 
                'Animations',
            },
        ],
    }

    return render(request, 'sketchbook.html', context)


# Create your views here.
