# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_contact'),
        ('miniLibrary', '0006_auto_20170420_0343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('body', models.TextField(blank=True, max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('total_likes', models.PositiveIntegerField(default=0)),
                ('auth', models.ForeignKey(verbose_name='作者', to='account.Profile', related_name='comments')),
                ('topic', models.ForeignKey(related_name='comments', to='miniLibrary.Topic')),
                ('user_likes', models.ManyToManyField(related_name='topic_liked', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='TopicProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('total_likes', models.PositiveIntegerField(default=0)),
                ('total_boomarks', models.PositiveIntegerField(default=0)),
                ('comments', models.ManyToManyField(related_name='comments', blank=True, to='miniLibrary.Comment')),
                ('topic', models.OneToOneField(to='miniLibrary.Topic', related_name='profile')),
                ('user_bookmarks', models.ManyToManyField(related_name='bookmarked', blank=True, to='account.Profile')),
                ('user_likes', models.ManyToManyField(related_name='topic_liked', blank=True, to='account.Profile')),
            ],
        ),
    ]
