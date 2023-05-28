from django.urls import path, include

from softuni_petstagram.pets import views

urlpatterns = [
    path("add/", views.add_pet, name="add pet"),
    path("<int:pk>/", include([
        path("", views.pet_details, name="pet details"),
        path("edit/", views.edit_pet, name="edit pet"),
        path("delete/", views.delete_pet, name="delete pet"),
    ])),
]
