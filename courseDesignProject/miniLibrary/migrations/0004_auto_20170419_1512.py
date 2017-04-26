# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniLibrary', '0003_remove_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='published',
        ),
        migrations.AddField(
            model_name='topic',
            name='status',
            field=models.CharField(max_length=20, choices=[('published', '审核通过'), ('wait', '等待审核'), ('ban', '审核不通过')], default='wait'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='category',
            field=models.ForeignKey(to='miniLibrary.Category', related_name='topics'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='files',
            field=models.FileField(upload_to='files/%Y/%m/%d', blank=True),
        ),
    ]
