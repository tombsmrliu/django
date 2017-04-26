# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniLibrary', '0010_auto_20170420_0822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': '主题', 'ordering': ('created',), 'verbose_name_plural': '主题'},
        ),
    ]
