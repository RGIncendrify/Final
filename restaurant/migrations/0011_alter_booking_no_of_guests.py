# Generated by Django 3.2.24 on 2024-02-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_auto_20240225_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
