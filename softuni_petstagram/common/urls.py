from django.urls import path

from softuni_petstagram.common import views

urlpatterns = [
    path("", views.index, name="index"),
]
