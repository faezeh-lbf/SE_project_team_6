from django.test import TestCase

from django.contrib.auth.models import User
from divar.models import Stuff
from divar.models import UserProfile


class StuffModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods

        user=User.objects.create_user(username="mahsa@gmail.com")
        user_profile=UserProfile.objects.create(user=user, phone_number="12345678")
        Stuff.objects.create(name='mobile A5', owner=user_profile, price=30, city='shiraz')

    def test_name_label(self):
        stuff = Stuff.objects.get(id=1)
        field_label = stuff._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_price_label(self):
        stuff=Stuff.objects.get(id=1)
        field_label = stuff._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_city_label(self):
        stuff=Stuff.objects.get(id=1)
        field_label = stuff._meta.get_field('city').verbose_name
        self.assertEquals(field_label, 'city')

    # def test_isFoori_label(self):
    #     stuff = Stuff.objects.get(id=1)
    #     field_label = stuff._meta.get_field('is_foori').verbose_name
    #     self.assertEquals(field_label, False)

    def test_name_max_length(self):
        stuff = Stuff.objects.get(id=1)
        max_length = stuff._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)

    def test_description_max_length(self):
        stuff = Stuff.objects.get(id=1)
        max_length = stuff._meta.get_field('description').max_length
        self.assertEquals(max_length, 900)


