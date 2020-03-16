# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-07 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20200307_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.CharField(choices=[('LOW', 'Low'), ('NORMAL', 'Normal'), ('HIGH', 'High')], default='LOW', max_length=20),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('NEW', 'New'), ('INPROGRESS', 'In Progress'), ('TESTING', 'Testing'), ('COMPLETED', 'Completed')], default='NEW', max_length=20),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='type',
            field=models.CharField(choices=[('BUG', 'Bug'), ('FEATURE', 'Feature')], default='BUG', max_length=20),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]