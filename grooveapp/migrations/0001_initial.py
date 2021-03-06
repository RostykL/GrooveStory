# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-19 09:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('num_stars', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_author_name', models.CharField(max_length=50)),
                ('last_author_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='grstory',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grooveapp.Posts'),
        ),
    ]
