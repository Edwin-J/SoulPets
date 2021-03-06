# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 14:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('kind', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=20)),
                ('rating', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
