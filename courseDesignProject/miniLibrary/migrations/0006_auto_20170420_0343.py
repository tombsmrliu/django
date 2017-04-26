# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('miniLibrary', '0005_auto_20170420_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='auth',
            field=models.ForeignKey(verbose_name='作者', related_name='topics', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topic',
            name='category',
            field=models.ForeignKey(verbose_name='分类', related_name='topics', to='miniLibrary.Category'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(blank=True, verbose_name='详情描述'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='files',
            field=models.FileField(blank=True, upload_to='files/%Y/%m/%d/', verbose_name='附件'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='status',
            field=models.CharField(default='wait', max_length=20, choices=[('published', '审核通过'), ('wait', '等待审核'), ('ban', '审核不通过')], verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
    ]
