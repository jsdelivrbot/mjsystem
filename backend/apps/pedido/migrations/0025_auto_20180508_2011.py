# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-08 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0024_auto_20180508_2008'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NrPedido',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='id',
        ),
        migrations.AddField(
            model_name='pedido',
            name='codigo',
            field=models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='Codigo'),
        ),
    ]
