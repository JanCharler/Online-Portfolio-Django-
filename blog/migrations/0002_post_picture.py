# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-20 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, upload_to='blog/media'),
        ),
    ]
