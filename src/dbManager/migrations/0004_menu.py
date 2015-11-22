# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbManager', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parentid', models.IntegerField()),
                ('level', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('isenable', models.IntegerField(default=0)),
            ],
        ),
    ]
