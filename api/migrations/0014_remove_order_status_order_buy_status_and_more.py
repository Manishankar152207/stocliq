# Generated by Django 4.1.5 on 2023-01-13 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_clientlog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='buy_status',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='buy_status_message',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='order',
            name='sell_status',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='sell_status_message',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='client',
            name='createdon',
            field=models.DateField(default=datetime.date(2023, 1, 13)),
        ),
        migrations.AlterField(
            model_name='clientlog',
            name='logout',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='buytime',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.date(2023, 1, 13)),
        ),
        migrations.AlterField(
            model_name='order',
            name='selltime',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
