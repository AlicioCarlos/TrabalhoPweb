# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controleacademico', '0006_auto_20161010_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='professor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='controleacademico.Professor'),
            preserve_default=False,
        ),
    ]
