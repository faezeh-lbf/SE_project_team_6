from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)


class Classtering(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

class Stuff(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.CharField(max_length=900)
    is_foori = models.BooleanField(default=False)
    has_pic = models.BooleanField(default=False)
    city = models.CharField(max_length=30, default='Tehran')
    location = models.CharField(max_length=30)
    classtering = models.ForeignKey(Classtering, on_delete=models.CASCADE, null=True)
    picture_loc = models.ImageField(blank=True, null=True, upload_to= "stuff_images")