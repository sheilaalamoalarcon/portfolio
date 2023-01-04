from django.urls import path
from portfolioWeb import views

urlpatterns = [
    path("", views.home, name="home"),
]