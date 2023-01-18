from django.shortcuts import render
from django.http import HttpResponse
import re

# al the def here will be our pages


def home(request):
    context = {
        'aboutMeText': 'Mi nombre es Sheila Álamo, bienvenidos/as a mi portafolio web, aquí encontrarás mis trabajos más recientes. Soy una persona altamente creativa y con mucha energía, aunque a veces puedo ser algo tímida. Me gradué como técnico de imagen especializado en la ilustración en la EADSGC, más tarde hice los siguientes cursos en la SPEGC: “Diseño UI/UX”, ”Programación Full-Stack”,”Especialización en ML” ',
        'socials': [
            {
                'https://www.instagram.com/sheila_ilustraciones', 
                'icons/instagram-logo.svg'
            },
            {
                'https://www.artstation.com/sheila-alamo-ilustraciones',
                'icons/artstation-logo.svg'
            },
            {
                'https://www.linkedin.com/in/sheila-%C3%A1lamo-alarc%C3%B3n-ilustraciones/',
                'icons/linkedin-logo.svg'
            },
        ],
        'menu': [
            {
                '/curriculum',
                'Curriculum'
            },
            {
                '/sketchbook', 
                'SketchBook'
            },
            {
                '/animations', 
                'Animations'
            },
        ],
        'uiDesign': [
            {
                'https://hayile.netlify.app/',
                'Hayile',
                'artwork-images/hayile/hayile-big-image.png',
                'artwork-images/hayile/hayile-small-image.png',
                'artwork-images/hayile/hayile-second-small-image.png'
            },
            {
                'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley',
                'Naturmode',
                'artwork-images/naturmode/naturmode-big-image.png',
                'artwork-images/naturmode/naturmode-small-image.png',
                'artwork-images/naturmode/naturmode-second-small-image.png'
            },
        ],
        'characterDesign': [
            {
                'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley',
                'Smile',
                'artwork-images/character-design/character-design-big-image.png',
                'artwork-images/character-design/character-design-small-image.png',
                'artwork-images/character-design/character-design-second-small-image.png'
            },
        ],
        'conceptDesign': [
            {
                'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley',
                'Concept Paintings',
                'artwork-images/concept-design/concept-paintings/concept-design-big-image.png',
                'artwork-images/concept-design/concept-paintings/concept-design-small-image.png',
                'artwork-images/concept-design/concept-paintings/concept-design-second-small-image.png'
            },
        ],
    }
    return render(request, 'base.html', context)


def Animations(request):
    
    return render(request, 'animations.html', )


def Curriculum(request):
    context = {
    'socials': [
        {
            'https://www.instagram.com/sheila_ilustraciones', 
            'icons/instagram-logo.svg'
        },
        {
            'https://www.artstation.com/sheila-alamo-ilustraciones',
            'icons/artstation-logo.svg'
        },
        {
            'https://www.linkedin.com/in/sheila-%C3%A1lamo-alarc%C3%B3n-ilustraciones/',
            'icons/linkedin-logo.svg'
        },
    ],
    'menu': [
            {
                '/sketchbook', 
                'SketchBook',
            },
            {
                '/animations', 
                'Animations',
            },
        ],
    'firstColumns': [
             {
                'icons/skills/html.svg',
                'HTML'
            },
            {
                'icons/skills/css.svg',
                'CSS'
            },
            {
                'icons/skills/javascript.svg',
                'JavaScript'
            },
            {
                'icons/skills/typescript.svg',
                'Typescript',
            },
            {
                'icons/skills/react.svg',
                'InDesign'
            },
            {
                'icons/skills/illustrator.svg',
                'Illustrator'
            },
            {
                'icons/skills/photoshop.svg',
                'Photoshop'
            },
        ],
        
    'secondColumns': [
            {
                'icons/skills/after-effects.svg',
                'After Effects'
            },
            {
                'icons/skills/animate.svg',
                'animate'
            },
            {
                'icons/skills/xd.svg',
                'XD'
            },
            {
                'icons/skills/figma.svg',
                'Figma'
            },
            {
                'icons/skills/zbrush.svg',
                'zbrush'
            },
            {
                'icons/skills/blender.svg',
                'blender'
            },
            {
                'icons/skills/unity.svg',
                'unity'
            }
        ],
    }

    return render(request, 'curriculum.html', context)


def SketchBook(request):
    
    return render(request, 'sketchbook.html')


# Create your views here.
