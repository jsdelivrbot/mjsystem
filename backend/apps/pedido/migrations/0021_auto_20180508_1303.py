# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-08 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0020_auto_20180508_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='bairro',
            field=models.CharField(default=None, max_length=255, verbose_name='Bairro'),
        ),
    ]
