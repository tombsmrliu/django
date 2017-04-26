# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniLibrary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=models.SlugField(max_length=200, blank=True),
        ),
    ]
