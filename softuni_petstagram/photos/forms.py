from django import forms

from softuni_petstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

        labels = {
            'tagged_pets': 'Tag Pets'
        }


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta(PhotoBaseForm.Meta):
        exclude = ('photo',)
