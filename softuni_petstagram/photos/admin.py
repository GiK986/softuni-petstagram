from django.contrib import admin
from softuni_petstagram.photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_tagged_pets', 'location', 'date_of_publication')

    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join([p.name for p in obj.tagged_pets.all()])
