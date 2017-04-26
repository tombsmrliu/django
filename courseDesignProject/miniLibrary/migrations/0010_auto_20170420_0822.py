# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniLibrary', '0009_auto_20170420_0703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created'], 'verbose_name_plural': '评论', 'verbose_name': '评论'},
        ),
        migrations.AlterModelOptions(
            name='topicprofile',
            options={'verbose_name_plural': "'主题'面板", 'verbose_name': "'主题'面板"},
        ),
        migrations.RenameField(
            model_name='topicprofile',
            old_name='total_boomarks',
            new_name='total_bookmarks',
        ),
        migrations.RemoveField(
            model_name='topicprofile',
            name='comments',
        ),
    ]
