# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-17 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0001_sale-model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('total_value', models.DecimalField(decimal_places=3, default=0, max_digits=10, null=True, verbose_name='Total Value')),
                ('pay_at', models.DateField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Sale')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
