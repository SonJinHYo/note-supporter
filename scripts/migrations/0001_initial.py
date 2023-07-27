# Generated by Django 4.2.3 on 2023-07-27 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Audio",
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
                ("data_url", models.URLField()),
                ("title", models.CharField(max_length=50)),
                ("origin_script", models.TextField()),
                ("modified_script", models.TextField()),
                ("create_at", models.DateTimeField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="audios",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Charecter",
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
                ("start_time", models.FloatField()),
                ("end_time", models.FloatField()),
                ("confidence", models.FloatField()),
                ("content", models.CharField(max_length=150)),
                ("type", models.CharField(max_length=20)),
                (
                    "script",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="charecters",
                        to="scripts.audio",
                    ),
                ),
            ],
        ),
    ]
