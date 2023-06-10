from django.contrib import admin
from softuni_petstagram.pets.models import Pet


# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'personal_photo', 'date_of_birth', 'slug')
