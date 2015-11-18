# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='manager',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='manager',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
