# Generated by Django 3.2.24 on 2024-02-21 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_bookingform'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookingForm',
        ),
    ]