# Generated by Django 4.1.5 on 2023-01-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_clientlog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientlog',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
