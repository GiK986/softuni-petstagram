from django.urls import path

from softuni_petstagram.common import views

urlpatterns = [
    path("", views.index, name="index"),
    path("like/<int:photo_id>/", views.like_functionality, name="like"),
]
