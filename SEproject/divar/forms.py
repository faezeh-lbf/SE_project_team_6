from django import forms
from .models import Stuff


class ItemForm(forms.ModelForm):

    class Meta:
        model = Stuff
        fields = ['name', 'price', 'description', 'location']
