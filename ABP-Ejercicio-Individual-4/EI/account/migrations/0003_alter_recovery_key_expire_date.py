# Generated by Django 5.0.4 on 2024-05-14 00:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_recovery_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recovery_key',
            name='expire_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]