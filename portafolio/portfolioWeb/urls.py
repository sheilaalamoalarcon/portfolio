from django.urls import path
from portfolioWeb import views

urlpatterns = [
    path("", views.home, name="home"),
    path("animations", views.Animations, name="animations"),
    path("curriculum", views.Curriculum, name="curriculum"),
    path("sketchbook", views.SketchBook, name="sketchbook"),

]
