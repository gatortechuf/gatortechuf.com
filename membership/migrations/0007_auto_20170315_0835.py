# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-15 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0006_auto_20170315_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinator',
            name='coordinator_image',
            field=models.ImageField(blank=True, upload_to='membership'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='leader_image',
            field=models.ImageField(blank=True, upload_to='membership'),
        ),
    ]
