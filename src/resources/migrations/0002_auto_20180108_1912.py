# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-09 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcefile',
            name='resource_file',
            field=models.FileField(max_length=1024, upload_to='resources'),
        ),
    ]
