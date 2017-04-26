# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniLibrary', '0011_auto_20170420_1523'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ('-created',), 'verbose_name': '主题', 'verbose_name_plural': '主题'},
        ),
    ]
