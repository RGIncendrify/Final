# Generated by Django 3.2.24 on 2024-02-26 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_remove_mine_no_of_guests'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]