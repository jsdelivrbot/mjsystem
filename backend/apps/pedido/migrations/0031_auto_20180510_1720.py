# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-10 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0030_auto_20180510_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='entrega',
            field=models.ForeignKey(default=0.09090909090909091, on_delete=django.db.models.deletion.CASCADE, to='pedido.Entrega'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.Cliente'),
        ),
    ]
