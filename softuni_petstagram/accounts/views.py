from django.shortcuts import render


# Create your views here.
def register_user(request):
    return render(request, 'accounts/register-page.html')


def login_user(request):
    return render(request, 'accounts/login-page.html')


def logout_user(request):
    return None


def profile_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_profile(request):
    return render(request, 'accounts/profile-edit-page.html')


def delete_profile(request):
    return render(request, 'accounts/profile-delete-page.html')
