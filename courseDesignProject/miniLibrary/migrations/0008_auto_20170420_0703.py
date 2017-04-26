# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('miniLibrary', '0007_comment_topicprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='comment_liked'),
        ),
        migrations.AlterField(
            model_name='topicprofile',
            name='user_likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='topic_liked'),
        ),
    ]
