# Generated by Django 3.2.7 on 2021-09-26 21:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.FloatField()),
                ('tax', models.IntegerField(default=15)),
                ('total', models.FloatField()),
                ('date', models.DateField(default=datetime.datetime(2021, 9, 26, 17, 53, 15, 407297))),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='calculator.discount')),
            ],
        ),
    ]
