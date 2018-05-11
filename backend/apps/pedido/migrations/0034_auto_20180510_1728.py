# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-10 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0033_auto_20180510_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrega',
            name='obs',
        ),
        migrations.AddField(
            model_name='pedido',
            name='obs',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Observações'),
        ),
    ]
