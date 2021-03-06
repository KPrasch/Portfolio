# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-01 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('height_in', models.IntegerField()),
                ('width_in', models.IntegerField()),
                ('description', models.TextField()),
                ('finish_date', models.DateTimeField()),
                ('created', models.DateTimeField()),
                ('small_image', models.ImageField(upload_to=b'')),
                ('large_image', models.ImageField(upload_to=b'')),
                ('draft', models.BooleanField(default=True)),
            ],
        ),
    ]
