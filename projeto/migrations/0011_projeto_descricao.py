# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0010_auto_20170726_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]