# Generated by Django 4.2a1 on 2023-02-17 21:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="file",
            field=models.ImageField(upload_to="room_photos"),
        ),
    ]
