# Generated by Django 5.0.1 on 2024-01-26 21:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0004_carinventory"),
    ]

    operations = [
        migrations.RenameField(
            model_name="carinventory",
            old_name="car_value",
            new_name="cars_value",
        ),
    ]
