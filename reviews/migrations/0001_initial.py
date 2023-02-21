# Generated by Django 4.2a1 on 2023-02-13 16:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("review", models.TextField()),
                ("accuracy", models.IntegerField()),
                ("communication", models.IntegerField()),
                ("cleanliness", models.IntegerField()),
                ("location", models.IntegerField()),
                ("check_in", models.IntegerField()),
                ("value", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
