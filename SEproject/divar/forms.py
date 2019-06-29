from django import forms
from django.forms import ChoiceField

from .models import Stuff, Classtering3, Classtering2, Classtering1


class ItemForm(forms.ModelForm):

    class Meta:
        model = Stuff
        fields = ['name', 'price', 'city', 'description', 'location', 'classtering3', 'picture', 'is_foori']
