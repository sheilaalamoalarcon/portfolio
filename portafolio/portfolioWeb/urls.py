from django.urls import path
from portfolioWeb import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about-me", views.AboutMe, name="about-me"),
    path("curriculum", views.Curriculum, name="curriculum"),
    path("sketchbook", views.SketchBook, name="sketchbook"),

]
