# Generated by Django 4.1.5 on 2023-01-04 19:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_client_createdon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='createdon',
            field=models.DateField(default=datetime.date(2023, 1, 4)),
        ),
        migrations.AlterField(
            model_name='order',
            name='buytime',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.date(2023, 1, 4)),
        ),
        migrations.AlterField(
            model_name='order',
            name='selltime',
            field=models.CharField(max_length=100),
        ),
    ]
