from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)


class Classtering1(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Classtering2(models.Model):
    name = models.CharField(max_length=30)
    parent = models.OneToOneField(Classtering1, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name


class Classtering3(models.Model):
    name = models.CharField(max_length=30)
    parent = models.OneToOneField(Classtering2, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name


class Stuff(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.CharField(max_length=900)
    is_foori = models.BooleanField(default=False)
    has_pic = models.BooleanField(default=False)
    city = models.CharField(max_length=30, default='Tehran')
    location = models.CharField(max_length=30)
    classtering3 = models.ForeignKey(Classtering3, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%D/', default='media/default.jpg')

    # def __str__(self):
    #     return self.name
    # photo = models.ImageField(upload_to='stuffImages')


class Favorite(models.Model):
    item = models.ForeignKey(Stuff)
    user = models.ForeignKey(UserProfile)
