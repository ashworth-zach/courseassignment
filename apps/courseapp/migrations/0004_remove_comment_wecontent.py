# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-15 14:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0003_comment_wecontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='wecontent',
        ),
    ]
