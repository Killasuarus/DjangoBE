# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logres', '0001_initial'),
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='wish',
            field=models.ManyToManyField(related_name='list_items', to='logres.User'),
        ),
    ]
