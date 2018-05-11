# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-11 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0039_auto_20180511_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrega',
            options={'verbose_name': 'Entrega', 'verbose_name_plural': 'Entregas'},
        ),
        migrations.RemoveField(
            model_name='entrega',
            name='codigo',
        ),
        migrations.AddField(
            model_name='entrega',
            name='id',
            field=models.AutoField(auto_created=True, default=0.09090909090909091, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
