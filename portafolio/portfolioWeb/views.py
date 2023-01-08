from django.shortcuts import render
from django.http import HttpResponse
import re
from django.utils.timezone import datetime

# al the def here will be our pages


def home(request):
    context = {
        'aboutMeText': 'Mi nombre es Sheila Álamo y bienvenidos/as a mi portafolio web, aquí encontrarás mis trabajos. Soy una persona altamente creativa y con mucha energía, aunque a veces puedo ser algo tímida. Me gradué como técnica en imagen especializada en la ilustración en la EADSGC, más tarde hice los siguientes cursos en la SPEGC: “Diseño UI/UX”, ”Programación Full-Stack”,”Especialización en ML” ',
        'socials': [
            {
                'https://www.instagram.com/sheila_ilustraciones', 
                '/instagram-logo.svg'
            },
            {
                'https://www.artstation.com/sheila-alamo-ilustraciones',
                '/artstation-logo.svg'
            },
            {
                'https://www.linkedin.com/in/sheila-%C3%A1lamo-alarc%C3%B3n-ilustraciones/',
                '/linkedin-logo.svg'
            },
        ],
        'menu': [
            {
                '/curriculum',
                'Curriculum',
            },
            {
                '/sketchbook', 
                'SketchBook',
            },
        ],
        
        'title' : 'Ilustración',
        'artwork': [
            {
                'https://hayile.netlify.app/',
                'Hayile',
                'artwork-images/hayile/hayile-big-image.png',
                'artwork-images/hayile/hayile-small-image.png', 
                'artwork-images/hayile/hayile-second-small-image.png',
            },
        ],
    }
    return render(request, 'header.html', context)


def AboutMe(request):

    return render(request, 'header.html')


def Curriculum(request):

    return render(request, 'header.html')


def SketchBook(request):

    return render(request, 'header.html')


# Create your views here.
