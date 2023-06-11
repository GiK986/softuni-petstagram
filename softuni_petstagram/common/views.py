from django.shortcuts import render

from softuni_petstagram.photos.models import Photo


# Create your views here.
def index(request):
    all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos,
    }

    return render(request, 'common/home-page.html', context=context)
