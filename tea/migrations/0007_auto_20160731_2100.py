# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tea', '0006_auto_20160731_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='products_photo'),
        ),
    ]