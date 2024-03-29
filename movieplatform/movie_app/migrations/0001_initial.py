# Generated by Django 5.0.1 on 2024-01-29 02:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category_movie",
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
                ("title", models.CharField(max_length=250, unique=True)),
                ("slug", models.SlugField(max_length=250, unique=True)),
                ("description", models.TextField(blank=True)),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=250, unique=True)),
                ("slug", models.SlugField(max_length=250, unique=True)),
                ("poster", models.ImageField(blank=True, upload_to="gallery")),
                ("description", models.TextField(blank=True)),
                ("release_date", models.DateField()),
                ("actors", models.CharField(max_length=250, unique=True)),
                ("trailer_link", models.URLField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movie_app.category_movie",
                    ),
                ),
            ],
            options={
                "verbose_name": "movie",
                "verbose_name_plural": "movies",
                "ordering": ("title",),
            },
        ),
    ]
