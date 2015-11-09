# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('grade', models.IntegerField()),
                ('goodComment', models.TextField()),
                ('badComment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('grade', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
