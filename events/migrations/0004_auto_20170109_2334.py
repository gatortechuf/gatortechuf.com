# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-10 04:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_delete_eventtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_description',
            field=models.TextField(default='Description', max_length=4096, verbose_name='Description'),
        ),
    ]