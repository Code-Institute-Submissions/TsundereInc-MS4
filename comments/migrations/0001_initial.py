# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-09 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=524)),
                ('date', models.DateField()),
                ('author', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
