# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-06-29 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divar', '0002_remove_stuff_picture_loc'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuff',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%D/'),
        ),
    ]
