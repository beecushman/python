# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagination_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='NULL', max_length=254),
            preserve_default=False,
        ),
    ]
