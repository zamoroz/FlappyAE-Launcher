# Generated by Django 5.0.1 on 2024-01-23 06:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_main", "0003_update_lang"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="lang",
            field=models.CharField(
                choices=[("RU", "ru"), ("EN", "en")],
                default="RU",
                max_length=2,
                verbose_name="Язык",
            ),
        ),
    ]
