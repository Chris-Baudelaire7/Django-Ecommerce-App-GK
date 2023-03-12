# Generated by Django 4.1.7 on 2023-03-11 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("category_name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField(blank=True, max_length=255, unique=True)),
                ("description", models.CharField(blank=True, max_length=255)),
                (
                    "cat_image",
                    models.ImageField(blank=True, upload_to="photos/categories"),
                ),
            ],
        ),
    ]
