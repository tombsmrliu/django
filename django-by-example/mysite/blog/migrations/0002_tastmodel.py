# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tastModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='yes', max_length=5)),
            ],
        ),
    ]