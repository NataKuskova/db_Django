# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tea', '0004_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='None', upload_to='products_photo'),
        ),
    ]
