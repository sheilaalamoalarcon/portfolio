from django.shortcuts import render
import requests

def home(request):
    context = {
        'socials': [
                {'link': 'https://www.instagram.com/sheila_ilustraciones/', 'imageDir': '/icons/instagram-logo.svg'},
                {'link': 'https://www.artstation.com/sheila-alamo-ilustraciones', 'imageDir': '/icons/artstation-logo.svg'},
                {'link': 'https://www.linkedin.com/in/sheila-%C3%A1lamo-alarc%C3%B3n-ilustraciones/', 'imageDir': '/icons/linkedin-logo.svg'},
            ],
        'pages': [
                {'link': '/sketchbook', 'name': 'Sketchbook'},
                {'link': '/animations', 'name': 'Animations'},
                {'link': '/curriculum', 'name': 'Curriculum'},
            ],
        'artworks': [
                {'title':'Hayile','path':'https://hayile.netlify.app/', 'firstImg':'/artwork-images/hayile/hayile-big-image.png', 'secondImg':'/artwork-images/hayile/hayile-small-image.png', 'thirdImg':'/artwork-images/hayile/hayile-second-small-image.png'},
                {'title':'Naturmode','path':'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley', 'firstImg':'/artwork-images/naturmode/naturmode-big-image.png', 'secondImg':'/artwork-images/naturmode/naturmode-small-image.png', 'thirdImg':'/artwork-images/naturmode/naturmode-second-small-image.png'},
            ]
    }
    
    return render(request, 'base.html', context)


def Animations(request):
    context = {
        'socials': [
                {'link': 'https://www.instagram.com/sheila_ilustraciones/', 'imageDir': '/icons/instagram-logo.svg'},
                {'link': 'https://www.artstation.com/sheila-alamo-ilustraciones', 'imageDir': '/icons/artstation-logo.svg'},
                {'link': 'https://www.linkedin.com/in/sheila-%C3%A1lamo-alarc%C3%B3n-ilustraciones/', 'imageDir': '/icons/linkedin-logo.svg'},
            ],
        'pages': [
                {'link': '/sketchbook', 'name': 'Sketchbook'},
                {'link': '/curriculum', 'name': 'curriculum'},
            ],
    }
    
    return render(request, 'animations.html', context )


def Curriculum(request):
    context = {
        'socials': [
                {'link': 'https://www.instagram.com/sheila_ilustraciones/', 'imageDir': '/icons/instagram-logo.svg'},
                {'link': 'https://www.artstation.com/sheila-alamo-ilustraciones', 'imageDir': '/icons/artstation-logo.svg'},
                {'link': 'https://www.linkedin.com/in/sheila-%C3%A1lamo-alarc%C3%B3n-ilustraciones/', 'imageDir': '/icons/linkedin-logo.svg'},
            ],
        'pages': [
                {'link': '/sketchbook', 'name': 'Sketchbook'},
                {'link': '/animations', 'name': 'Animations'},
            ],
        'skills': [
                {"name":'HTML', 'imageDir':'/icons/skills/html.svg'},
                {"name":'CSS', 'imageDir':'/icons/skills/css.svg'},
                {"name":'JavaScript', 'imageDir':'/icons/skills/javascript.svg'},
                {"name":'Typescript', 'imageDir':'/icons/skills/typescript.svg'},
                {"name":'InDesign', 'imageDir':'/icons/skills/indesign.svg'},
                {"name":'Illustrator', 'imageDir':'/icons/skills/illustrator.svg'},
                {"name":'Photoshop', 'imageDir':'/icons/skills/photoshop.svg'},
                {"name":'After Effects', 'imageDir':'/icons/skills/after-effects.svg'},
                {"name":'Animate', 'imageDir':'/icons/skills/animate.svg'},
                {"name":'XD', 'imageDir':'/icons/skills/xd.svg'},
                {"name":'Figma', 'imageDir':'/icons/skills/figma.svg'},
                {"name":'Zbrush', 'imageDir':'/icons/skills/zbrush.svg'},
                {"name":'Blender', 'imageDir':'/icons/skills/blender.svg'},
                {"name":'Unity', 'imageDir':'/icons/skills/unity.svg'},
            ],
    }

    return render(request, 'curriculum.html', context)


def SketchBook(request):
    context = {
        'socials': [
            {'link': 'https://www.instagram.com/sheila_ilustraciones/', 'imageDir': '/icons/instagram-logo.svg'},
            {'link': 'https://www.artstation.com/sheila-alamo-ilustraciones', 'imageDir': '/icons/artstation-logo.svg'},
            {'link': 'https://www.linkedin.com/in/sheila-%C3%A1lamo-alarc%C3%B3n-ilustraciones/', 'imageDir': '/icons/linkedin-logo.svg'},
        ],
        'pages': [
            {'link': '/curriculum', 'name': 'Curriculum'},
            {'link': '/animations', 'name': 'Animations'},
        ],
        'sketches': [
            {'title': 'Sketch 1','imageDir': '/icons/instagram-logo.svg'},
        ],
    }
    
    return render(request, 'sketchbook.html', context)


# Create your views here.
