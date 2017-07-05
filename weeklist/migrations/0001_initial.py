# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_num', models.IntegerField(max_length=52)),
                ('washer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('room', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='week',
            name='Year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklist.Year'),
        ),
    ]
