# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-15 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epc',
            fields=[
                ('ns_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='ns.Ns')),
                ('heat', models.TextField(blank=True, null=True)),
            ],
            bases=('ns.ns',),
        ),
    ]
