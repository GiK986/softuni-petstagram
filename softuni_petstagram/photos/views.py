from django.shortcuts import render, redirect

from softuni_petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from softuni_petstagram.photos.models import Photo


# Create your views here.
def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'photos/photo-add-page.html',
        context=context
    )


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
    }

    return render(request, 'photos/photo-details-page.html', context=context)


def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'GET':
        form = PhotoEditForm(instance=photo)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo details', pk)

    context = {
        'form': form,
        'photo': photo,
    }

    return render(
        request,
        'photos/photo-edit-page.html',
        context=context
    )


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()

    return redirect('index')
