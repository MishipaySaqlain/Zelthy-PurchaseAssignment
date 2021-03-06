# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-14 20:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchaser_name', models.CharField(help_text='Name of the purchaser', max_length=256)),
                ('quantity', models.IntegerField(help_text='Purchase Quantity', validators=[django.core.validators.MinValueValidator(1)])),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'purchase',
            },
        ),
        migrations.CreateModel(
            name='PurchaseStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(1, 'Open'), (2, 'Verified'), (3, 'Dispatched'), (4, 'Delivered')], help_text='Status of the purchase.', max_length=25)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('purchase', models.ForeignKey(help_text='Purchase reference', on_delete=django.db.models.deletion.CASCADE, to='purchase.Purchase')),
            ],
            options={
                'db_table': 'purchase_status',
            },
        ),
        migrations.AlterUniqueTogether(
            name='purchasestatus',
            unique_together=set([('purchase', 'status')]),
        ),
    ]
