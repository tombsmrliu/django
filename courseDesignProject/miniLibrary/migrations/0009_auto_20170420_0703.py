# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('miniLibrary', '0008_auto_20170420_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='auth',
            field=models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL, related_name='comments'),
        ),
        migrations.AlterField(
            model_name='topicprofile',
            name='user_bookmarks',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='bookmarked'),
        ),
    ]
