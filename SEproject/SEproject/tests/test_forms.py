from django.test import TestCase
from django.test import Client
from divar.forms import ItemForm
from divar.forms import Stuff

class Setup_Class(TestCase):

    def setUp(self):
        self.stuff = Stuff.objects.create(name="pejho pars", price=3000, description="the color is black", location="shiraz-pasdaran blv.")

class ItemForm_Test(TestCase):

    # Valid Form Data
    def test_StuffForm_valid(self):
        form = ItemForm(data={'name':"pejho pars", 'price':3000, 'description':"the color is black", 'location':"shiraz-pasdaran blv."})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = ItemForm(data={'name': "", 'price': 3000, 'description': "", 'location': "shiraz-pasdaran blv."})
        self.assertFalse(form.is_valid())