# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controleacademico', '0011_auto_20161015_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='boletim',
            name='mediaNota',
            field=models.FloatField(default=1, verbose_name=(models.FloatField(), models.FloatField(), models.FloatField())),
            preserve_default=False,
        ),
    ]