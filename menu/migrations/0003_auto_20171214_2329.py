# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20171203_2315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='image',
            new_name='imgs',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='date',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='writer',
        ),
        migrations.AddField(
            model_name='pet',
            name='info',
            field=models.TextField(default='정보를 300자 이내로 작성하여 주세요.', max_length=300),
        ),
    ]
