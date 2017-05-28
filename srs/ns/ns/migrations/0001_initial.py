# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-28 03:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operators', '0001_initial'),
        ('vims', '0001_initial'),
        ('vnfs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('file', models.FileField(upload_to='opnfv/')),
                ('status', models.CharField(default='Shut Down', max_length=120)),
                ('price', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('vim_option', models.CharField(default='Near', max_length=120)),
                ('launch_time', models.DateTimeField(blank=True, null=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operators.Operator')),
                ('vim', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vims.Vim')),
            ],
            options={
                'ordering': ['-timestamp', '-update'],
            },
        ),
        migrations.CreateModel(
            name='Nvf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('mgmt_ip', models.CharField(blank=True, max_length=120, null=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('ns', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ns.Ns')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operators.Operator')),
                ('vnf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vnfs.Vnf')),
            ],
        ),
    ]
