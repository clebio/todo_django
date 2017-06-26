# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-25 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20170621_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='priority',
            field=models.FloatField(default=-1),
        ),
    ]