# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-28 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_leader_leader_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinator',
            name='coordinator_image',
            field=models.ImageField(blank=True, upload_to='membership'),
        ),
    ]
