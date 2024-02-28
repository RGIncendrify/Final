# Generated by Django 3.2.24 on 2024-02-27 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortintervalcontrol', '0007_rename_purificationplant_processplant'),
    ]

    operations = [
        migrations.CreateModel(
            name='DieselFleet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oil_changes', models.PositiveIntegerField(default=1)),
                ('battery_change', models.PositiveIntegerField(default=3)),
            ],
        ),
    ]
