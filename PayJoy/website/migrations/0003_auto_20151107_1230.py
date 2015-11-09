# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20151107_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='updateTime',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shop',
            name='updateTime',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
