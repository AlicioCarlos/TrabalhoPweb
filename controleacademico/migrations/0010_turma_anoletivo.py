# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controleacademico', '0009_auto_20161015_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='anoLetivo',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]
