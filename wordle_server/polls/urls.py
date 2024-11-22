from django.urls import path
from . import views

urlpatterns = [
    path("", view = views.index, name = "Index"),
    path("random", view = views.randomWord, name = "Random"),
    path("randomRange", view = views.randomRange, name = "Random range")
]