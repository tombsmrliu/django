# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniLibrary', '0004_auto_20170419_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='files',
            field=models.FileField(upload_to='files/%Y/%m/%d/', blank=True),
        ),
    ]
