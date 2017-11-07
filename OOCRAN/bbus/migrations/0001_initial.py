# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-06 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ns', '0001_initial'),
        ('scenarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bbu',
            fields=[
                ('nvf_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ns.Nvf')),
                ('freC_DL', models.PositiveIntegerField(blank=True, null=True)),
                ('color_DL', models.CharField(blank=True, default='#AA0000', max_length=20, null=True)),
                ('bw_dl', models.IntegerField(blank=True, null=True)),
                ('rb', models.IntegerField(blank=True, null=True)),
                ('pt', models.FloatField(blank=True, null=True)),
                ('freC_UL', models.PositiveIntegerField(blank=True, null=True)),
                ('color_UL', models.CharField(blank=True, max_length=20, null=True)),
                ('bw_ul', models.IntegerField(blank=True, null=True)),
                ('radio', models.CharField(blank=True, max_length=120, null=True)),
                ('is_simulate', models.BooleanField(default=False)),
                ('next_nvf', models.CharField(blank=True, max_length=120, null=True)),
                ('rrh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scenarios.RRH')),
            ],
            options={
                'ordering': ['-timestamp', '-update'],
            },
            bases=('ns.nvf',),
        ),
    ]