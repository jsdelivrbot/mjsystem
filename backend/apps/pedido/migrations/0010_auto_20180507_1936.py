# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-07 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0009_auto_20180507_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrega',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='cliente',
        ),
        migrations.AddField(
            model_name='cliente',
            name='entrega',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pedido.Entrega'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='pedido',
            field=models.ForeignKey(default=0.1, on_delete=django.db.models.deletion.CASCADE, to='pedido.Pedido'),
            preserve_default=False,
        ),
    ]
