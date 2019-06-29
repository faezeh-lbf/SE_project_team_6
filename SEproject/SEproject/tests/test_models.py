from django.test import TestCase

from django.contrib.auth.models import User
from divar.models import *


class StuffModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods

        user=User.objects.create_user(username="mahsa@gmail.com", password="mahsamahsa")
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

    def test_name_max_length(self):
        stuff = Stuff.objects.get(id=1)
        max_length = stuff._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)

    def test_description_max_length(self):
        stuff = Stuff.objects.get(id=1)
        max_length = stuff._meta.get_field('description').max_length
        self.assertEquals(max_length, 900)


class UserProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        user=User.objects.create_user(username="sahar@gmail.com", password="saharsahar")
        user_profile=UserProfile.objects.create(user=user, phone_number="12345679")

    def test_phoneNumber_label(self):
        user_profile = Stuff.objects.get(id=1)
        field_label = user_profile._meta.get_field('phone_number').verbose_name
        self.assertEquals(field_label, 'phone_number')

    def test_name_max_length(self):
        user_profile = Stuff.objects.get(id=1)
        max_length = user_profile._meta.get_field('phone_number').max_length
        self.assertEquals(max_length, 100)

class Clustering1ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        clustering1=Classtering1.objects.create(name="وسایل نقلیه")

    def test_name_label(self):
        clustering1 = Stuff.objects.get(id=1)
        field_label = clustering1._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        clustering1 = Stuff.objects.get(id=1)
        max_length = clustering1._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)

class Clustering2ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        clustering1=Classtering1.objects.create(name="وسایل نقلیه")
        clustering2=Classtering2.objects.create(name="خودرو", parent=clustering1)

    def test_name_label(self):
        clustering2 = Stuff.objects.get(id=1)
        field_label = clustering2._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        clustering1 = Stuff.objects.get(id=1)
        max_length = clustering1._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)

    def test_name_label(self):
        clustering2 = Stuff.objects.get(id=1)
        field_label = clustering2._meta.get_field('parent').verbose_name
        self.assertEquals(field_label, 'parent')

class Clustering2ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        clustering1=Classtering1.objects.create(name="وسایل نقلیه")
        clustering2=Classtering2.objects.create(name="خودرو", parent=clustering1)
        clustering3 = Classtering2.objects.create(name="سواری", parent=clustering2)

    def test_name_label(self):
        clustering3 = Stuff.objects.get(id=1)
        field_label = clustering3._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        clustering3 = Stuff.objects.get(id=1)
        max_length = clustering3._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)

    def test_name_label(self):
        clustering3 = Stuff.objects.get(id=1)
        field_label = clustering3._meta.get_field('parent').verbose_name
        self.assertEquals(field_label, 'parent')