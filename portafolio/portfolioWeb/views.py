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
                {'title':'Naturmode','path':'https://www.figma.com/proto/vchKAP63D4inZc2YMm3sCq/NATUREMODE?page-id=1%3A3&node-id=48%3A63&viewport=-2207%2C1126%2C0.42&scaling=scale-down&starting-point-node-id=2%3A155', 'firstImg':'/artwork-images/naturmode/naturmode-big-image.png', 'secondImg':'/artwork-images/naturmode/naturmode-first-small-image.png', 'thirdImg':'/artwork-images/naturmode/naturmode-second-small-image.png'},
                {'title':'Foodies','path':'https://www.figma.com/proto/TAN24kNs6nUlbOiYqqx2Ss/FOODIES?page-id=0%3A1&node-id=311%3A5859&viewport=646%2C436%2C0.14&scaling=scale-down&starting-point-node-id=311%3A5859', 'firstImg':'/artwork-images/foodies/foodies-big-image.png', 'secondImg':'/artwork-images/foodies/foodies-first-small-image.png', 'thirdImg':'/artwork-images/foodies/foodies-second-small-image.png'},
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
                {'link': '/curriculum', 'name': 'Curriculum'},
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
                {"name":'HTML', 'imageDir':'/icons/skills/html.svg', 'rating': '3/5'},
                {"name":'CSS', 'imageDir':'/icons/skills/css.svg', 'rating': '3/5'},
                {"name":'JavaScript', 'imageDir':'/icons/skills/javascript.svg', 'rating': '3/5'},
                {"name":'Typescript', 'imageDir':'/icons/skills/typescript.svg', 'rating': '3/5'},
                {"name":'InDesign', 'imageDir':'/icons/skills/indesign.svg', 'rating': '3/5'},
                {"name":'Illustrator', 'imageDir':'/icons/skills/illustrator.svg', 'rating': '3/5'},
                {"name":'Photoshop', 'imageDir':'/icons/skills/photoshop.svg', 'rating': '3/5'},
                {"name":'After Effects', 'imageDir':'/icons/skills/after-effects.svg', 'rating': '3/5'},
                {"name":'Animate', 'imageDir':'/icons/skills/animate.svg', 'rating': '3/5'},
                {"name":'XD', 'imageDir':'/icons/skills/xd.svg', 'rating': '3/5'},
                {"name":'Figma', 'imageDir':'/icons/skills/figma.svg', 'rating': '3/5'},
                {"name":'Zbrush', 'imageDir':'/icons/skills/zbrush.svg', 'rating': '3/5'},
                {"name":'Blender', 'imageDir':'/icons/skills/blender.svg', 'rating': '3/5'},
                {"name":'Unity', 'imageDir':'/icons/skills/unity.svg', 'rating': '3/5'},
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
            {'title': 'Sketch 1','imageDir': '/sketches/sketch-1.png'},
            {'title': 'Sketch 2','imageDir': '/sketches/sketch-2.png'},
            {'title': 'Sketch 3','imageDir': '/sketches/sketch-3.png'},
            {'title': 'Sketch 4','imageDir': '/sketches/sketch-4.png'},
            {'title': 'Sketch 5','imageDir': '/sketches/sketch-5.png'},
            {'title': 'Sketch 6','imageDir': '/sketches/sketch-6.jpeg'},
            {'title': 'Sketch 7','imageDir': '/sketches/sketch-7.jpg'},
            {'title': 'Sketch 8','imageDir': '/sketches/sketch-8.png'},
            {'title': 'Sketch 9','imageDir': '/sketches/sketch-9.png'},
            {'title': 'Sketch 10','imageDir': '/sketches/sketch-10.jpeg'},
        ],
    }
    
    return render(request, 'sketchbook.html', context)


# Create your views here.
