# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnterDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=5)),
                ('contact_no', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]