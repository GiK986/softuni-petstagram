from django import forms

from softuni_petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'Date of birth',
                    'type': 'date',
                }
            ),
            'personal_photo': forms.TextInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            ),
        }

        labels = {
            'name': 'Pet name',
            'date_of_birth': 'Date of birth',
            'personal_photo': 'Link to image',
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for (_, field) in self.fields.items():
            # field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
