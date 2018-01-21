# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-09 00:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20180108_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_link', models.CharField(max_length=1024)),
                ('resource_link_name', models.CharField(max_length=256)),
                ('resource_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Resource')),
            ],
        ),
    ]