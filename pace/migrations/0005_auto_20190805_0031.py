# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-05 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pace', '0004_announce'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='image',
            field=models.ImageField(upload_to='images3/'),
        ),
        migrations.AlterField(
            model_name='assign',
            name='image',
            field=models.ImageField(upload_to='images2/'),
        ),
    ]
