# Generated by Django 4.1 on 2022-09-02 03:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossapp', '0025_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
