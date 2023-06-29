from django.shortcuts import render, redirect

from softuni_petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from softuni_petstagram.pets.models import Pet


# Create your views here.
def add_pet(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk=1)

    context = {
        'form': form,
    }

    return render(
        request,
        'pets/pet-add-page.html',
        context=context
    )


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
    }

    return render(request, 'pets/pet-details-page.html', context=context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk=1)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(
        request,
        'pets/pet-edit-page.html',
        context=context
    )


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetDeleteForm(instance=pet)
    else:
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk=1)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(
        request,
        'pets/pet-delete-page.html',
        context=context
    )
