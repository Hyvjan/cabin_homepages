# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-13 21:41
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepages', '0003_pictures'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaturePictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_description', models.TextField()),
                ('file_up', models.FileField(blank=True, upload_to=b'')),
                ('url', autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='picture_description', unique=True)),
            ],
        ),
    ]
