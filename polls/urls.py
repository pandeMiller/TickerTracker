from django.urls import path

from . import views

urlpatterns = [
    path("tests/", views.index, name="index"),
]