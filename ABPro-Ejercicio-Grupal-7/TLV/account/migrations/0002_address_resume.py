# Generated by Django 5.0.4 on 2024-06-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='resume',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]