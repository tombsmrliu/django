# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200)),
                ('files', models.FileField(upload_to='files/%Y/%m/%d')),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=False)),
                ('auth', models.ForeignKey(related_name='topics', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(related_name='posts', to='miniLibrary.Category')),
            ],
            options={
                'verbose_name': '主题',
                'verbose_name_plural': '主题',
                'ordering': ('-created',),
            },
        ),
    ]
