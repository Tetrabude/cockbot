# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkeeper', '0007_extraingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=2048, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instruction',
            field=models.TextField(max_length=2048, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.URLField(max_length=256, default=''),
            preserve_default=True,
        ),
    ]
