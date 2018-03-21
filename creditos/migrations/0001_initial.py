# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('cae', models.DecimalField(decimal_places=2, max_digits=4)),
                ('im_1', models.DecimalField(decimal_places=2, max_digits=4)),
                ('im_2', models.DecimalField(decimal_places=2, max_digits=4)),
                ('im_3', models.DecimalField(decimal_places=2, max_digits=4)),
                ('im_4', models.DecimalField(decimal_places=2, max_digits=4)),
                ('seguro', models.IntegerField()),
                ('gastos', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
    ]
