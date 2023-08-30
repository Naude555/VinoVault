# Generated by Django 4.2.4 on 2023-08-13 16:09

from django.db import migrations, models
import django.utils.timezone
import vinventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('vinventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='date_received',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='wine',
            name='date_to_drink_end',
            field=models.DateField(default=vinventory.models.default_date_to_drink_end),
        ),
        migrations.AlterField(
            model_name='wine',
            name='date_to_drink_start',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]