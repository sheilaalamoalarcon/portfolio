from django.shortcuts import render
import requests


def home(request):
    context = {
        'socials': [
            {'link': 'https://www.instagram.com/sheila_ilustraciones/',
                'imageDir': '/icons/instagram-logo.svg'},
            {'link': 'https://www.artstation.com/sheila-alamo-ilustraciones',
                'imageDir': '/icons/artstation-logo.svg'},
            {'link': 'https://www.linkedin.com/in/sheila-%C3%A1lamo-alarc%C3%B3n-ilustraciones/',
                'imageDir': '/icons/linkedin-logo.svg'},
        ],
        'pages': [
            {'link': '/sketchbook', 'name': 'Sketchbook'},
            {'link': '/animations', 'name': 'Animations'},
            {'link': '/curriculum', 'name': 'Curriculum'},
        ],
        'artworks': [
            {'title': 'Hayile', 'path': 'https://hayile.netlify.app/', 'firstImg': '/artwork-images/hayile/big-image.png', 'secondImg': '/artwork-images/hayile/hayile-small-image.png',
                'thirdImg': '/artwork-images/hayile/hayile-second-small-image.png', 'description': 'Hayile is a web app that allows you to search for shortcuts. It was created on Angular by the DapperDrake Group.'},
            {'title': 'Naturmode', 'path': 'https://www.figma.com/proto/vchKAP63D4inZc2YMm3sCq/NATUREMODE?page-id=1%3A3&node-id=48%3A63&viewport=-2207%2C1126%2C0.42&scaling=scale-down&starting-point-node-id=2%3A155', 'firstImg': '/artwork-images/naturmode/big-image.png', 'secondImg': '/artwork-images/naturmode/naturmode-first-small-image.png',
             'thirdImg': '/artwork-images/naturmode/naturmode-second-small-image.png', 'description': 'Naturmode is a app that allow user to upload and search for clothes, is designed for clothing stores that will have item on a unsellable state or second hand clothing that still can be wear.'},
            {'title': 'Foodies', 'path': 'https://www.figma.com/proto/TAN24kNs6nUlbOiYqqx2Ss/FOODIES?page-id=0%3A1&node-id=311%3A5859&viewport=646%2C436%2C0.14&scaling=scale-down&starting-point-node-id=311%3A5859', 'firstImg': '/artwork-images/foodies/foodies-big-image.png', 'secondImg': '/artwork-images/foodies/foodies-first-small-image.png',
             'thirdImg': '/artwork-images/foodies/foodies-second-small-image.png', 'description': 'Foodies is an idea of app that will allow restaurants owners to upload their menu, see income and losses through the weeks, month and year and to track their employes performance.'},
        ]
    }

    return render(request, 'base.html', context)


def Animations(request):
    context = {
        'socials': [
            {'link': 'https://www.instagram.com/sheila_ilustraciones/',
                'imageDir': '/icons/instagram-logo.svg'},
            {'link': 'https://www.artstation.com/sheila-alamo-ilustraciones',
                'imageDir': '/icons/artstation-logo.svg'},
            {'link': 'https://www.linkedin.com/in/sheila-%C3%A1lamo-alarc%C3%B3n-ilustraciones/',
                'imageDir': '/icons/linkedin-logo.svg'},
        ],
        'pages': [
            {'link': '/sketchbook', 'name': 'Sketchbook'},
            {'link': '/curriculum', 'name': 'Curriculum'},
        ],
        'animations': [
            {'name': "Say Hi", 'imageDir': 'animations/animation-1.gif'},
            {'name': "Smile - Character Jumping Cicle",
                'imageDir': 'animations/animation-2.gif'},
            {'name': "Smile - Character Walking Cicle",
                'imageDir': 'animations/animation-3.gif'},
        ],
    }

    return render(request, 'animations.html', context)


def Curriculum(request):
    context = {
        'aboutMe': "Hi welcome to my portfolio, my name is Sheila Álamo, here you can see my artwork on design, illustration and animation, also you can sneak a peak into my sketchbook and see in what I'm working recently.",
        'socials': [
            {'link': 'https://www.instagram.com/sheila_ilustraciones/',
                'imageDir': '/icons/instagram-logo.svg'},
            {'link': 'https://www.artstation.com/sheila-alamo-ilustraciones',
                'imageDir': '/icons/artstation-logo.svg'},
            {'link': 'https://www.linkedin.com/in/sheila-%C3%A1lamo-alarc%C3%B3n-ilustraciones/',
                'imageDir': '/icons/linkedin-logo.svg'},
        ],
        'pages': [
            {'link': '/sketchbook', 'name': 'Sketchbook'},
            {'link': '/animations', 'name': 'Animations'},
        ],
        'skills': [
            {"name": 'HTML', 'imageDir': '/icons/skills/html.svg', 'rating': '2/5'},
            {"name": 'CSS', 'imageDir': '/icons/skills/css.svg', 'rating': '2/5'},
            {"name": 'JavaScript',
                'imageDir': '/icons/skills/javascript.svg', 'rating': '2/5'},
            {"name": 'Typescript',
                'imageDir': '/icons/skills/typescript.svg', 'rating': '2/5'},
            {"name": 'InDesign', 'imageDir': '/icons/skills/indesign.svg', 'rating': '4/5'},
            {"name": 'Illustrator',
                'imageDir': '/icons/skills/illustrator.svg', 'rating': '4/5'},
            {"name": 'Photoshop',
                'imageDir': '/icons/skills/photoshop.svg', 'rating': '4/5'},
            {"name": 'After Effects',
                'imageDir': '/icons/skills/after-effects.svg', 'rating': '2/5'},
            {"name": 'Animate', 'imageDir': '/icons/skills/animate.svg', 'rating': '2/5'},
            {"name": 'XD', 'imageDir': '/icons/skills/xd.svg', 'rating': '4/5'},
            {"name": 'Figma', 'imageDir': '/icons/skills/figma.svg', 'rating': '3/5'},
            {"name": 'Zbrush', 'imageDir': '/icons/skills/zbrush.svg', 'rating': '2/5'},
            {"name": 'Blender', 'imageDir': '/icons/skills/blender.svg', 'rating': '2/5'},
            {"name": 'Unity', 'imageDir': '/icons/skills/unity.svg', 'rating': '1/5'},
        ],
        'studies': [
            {'name': 'Bachillerato de Artes',  'endDate': '2018',
                'place': 'Escuela de Arte y Diseño de Gran Canaria'},
            {'name': 'Título de Técnico Superior en Artes Plásticas y Diseño en ilustración',
             'endDate': '2021', 'place': 'Escuela de Arte y Diseño de Gran Canaria'},
            {'name': 'Curso de Diseño UI/UX',
             'endDate': '2022', 'place': 'SPEGC'},
            {'name': 'Curso de Especialización en IA',
             'endDate': '2022', 'place': 'SPEGC'},
            {'name': 'Curso de FullStack',  'endDate': '2023', 'place': 'SPEGC'},
        ],
        'experiences': [
            {'name': 'Concept Artist',  'endDate': '2020',
                'company': 'Teatro Pérez Galdós - La Flauta Mágica'},
            {'name': 'Illustrator',  'endDate': '2019', 'company': 'Markeliñe'},
            {'name': 'Concept Artist & banner designer',  'endDate': '2020',
                'company': 'Jardín Botánico Viera y Clavijo'},
            {'name': 'Illustrator',  'endDate': '2021',
                'company': 'ADA Gran Canaria'},
        ],
        'aptitudes': [
            {'name': 'Creativity', 'type': 'personal'},
            {'name': 'Teamwork', 'type': 'social'},
            {'name': 'Problem Solving', 'type': 'personal'},
            {'name': 'Communication', 'type': 'social'},
            {'name': 'Adaptability', 'type': 'personal'},
            {'name': 'Time Management', 'type': 'personal'},
            {'name': 'English Level B2', 'type': 'idioms'},
            {'name': 'Spanish Level C1', 'type': 'idioms'},
            {'name': 'German Level A2', 'type': 'idioms'},
            {'name': 'Italian Level A2', 'type': 'idioms'},
        ],
    }

    return render(request, 'curriculum.html', context)


def SketchBook(request):
    context = {
        'socials': [
            {'link': 'https://www.instagram.com/sheila_ilustraciones/',
                'imageDir': '/icons/instagram-logo.svg'},
            {'link': 'https://www.artstation.com/sheila-alamo-ilustraciones',
                'imageDir': '/icons/artstation-logo.svg'},
            {'link': 'https://www.linkedin.com/in/sheila-%C3%A1lamo-alarc%C3%B3n-ilustraciones/',
                'imageDir': '/icons/linkedin-logo.svg'},
        ],
        'pages': [
            {'link': '/curriculum', 'name': 'Curriculum'},
            {'link': '/animations', 'name': 'Animations'},
        ],
        'sketches': [
            {'title': "Cow's Valley", 'imageDir': '/sketches/sketch-1.png'},
            {'title': "Cow's Valley Line", 'imageDir': '/sketches/sketch-2.png'},
            {'title': "Cow's Valley Color", 'imageDir': '/sketches/sketch-3.png'},
            {'title': 'Underwater Cave', 'imageDir': '/sketches/sketch-4.png'},
            {'title': 'Underwater Cave Line', 'imageDir': '/sketches/sketch-5.png'},
            {'title': 'Color Practice - Arcane',
                'imageDir': '/sketches/sketch-6.jpeg'},
            {'title': 'Simplification Practice - Nenè',
                'imageDir': '/sketches/sketch-7.jpg'},
            {'title': 'Simplification Practice - Lola Massieu',
                'imageDir': '/sketches/sketch-8.png'},
            {'title': 'Simplification Practice - Tamara de Lempicka',
                'imageDir': '/sketches/sketch-9.png'},
            {'title': 'Tiger Under 5 Minutes',
                'imageDir': '/sketches/sketch-10.jpeg'},
        ],
    }

    return render(request, 'sketchbook.html', context)
