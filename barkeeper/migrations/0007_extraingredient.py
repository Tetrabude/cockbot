# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkeeper', '0006_auto_20150327_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.CharField(max_length=56)),
                ('rawMaterial', models.CharField(max_length=56)),
                ('recipe', models.ForeignKey(to='barkeeper.Recipe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
