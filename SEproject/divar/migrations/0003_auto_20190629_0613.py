# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-06-29 06:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('divar', '0002_auto_20190629_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtering',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='divar.Classtering'),
        ),
    ]
