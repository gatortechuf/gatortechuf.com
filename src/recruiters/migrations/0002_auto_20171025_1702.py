# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 21:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SponsorshipLevels',
            new_name='SponsorshipLevel',
        ),
    ]
