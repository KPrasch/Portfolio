# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-02 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_piece_collage_placement'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='thumbnail_image',
            field=models.ImageField(default=1, upload_to=b''),
            preserve_default=False,
        ),
    ]
