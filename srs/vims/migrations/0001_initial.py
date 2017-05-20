# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-15 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=120)),
                ('vendor_id', models.CharField(max_length=4)),
                ('product_id', models.CharField(max_length=4)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('type', models.CharField(max_length=120)),
                ('ip', models.CharField(max_length=120)),
                ('latitude', models.FloatField(max_length=120)),
                ('longitude', models.FloatField(max_length=120)),
                ('username', models.CharField(default='admin', max_length=120)),
                ('password', models.CharField(blank=True, max_length=120, null=True)),
                ('project_domain', models.CharField(default='default', max_length=120)),
                ('project', models.CharField(default='admin', max_length=120)),
                ('public_network', models.CharField(default='network', max_length=120)),
                ('domain', models.CharField(default='default', max_length=120)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='vim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vims.Vim'),
        ),
    ]
