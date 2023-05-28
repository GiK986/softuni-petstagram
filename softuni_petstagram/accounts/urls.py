from django.urls import path, include

from softuni_petstagram.accounts import views


urlpatterns = [
    path("register/", views.register_user, name="register user"),
    path("login/", views.login_user, name="login user"),
    path("logout/", views.logout_user, name="logout user"),
    path("profile/<int:pk>", include([
        path("", views.profile_details, name="profile details"),
        path("edit/", views.edit_profile, name="edit profile"),
        path("delete/", views.delete_profile, name="delete profile"),
    ])),
]
