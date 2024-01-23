# Generated by Django 5.0.1 on 2024-01-23 05:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_main", "0002_alter_update_previous_alter_update_update_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="update",
            name="lang",
            field=models.CharField(
                choices=[("RU", "ru"), ("EN", "en")],
                default="RU",
                max_length=2,
                verbose_name="Язык",
            ),
        ),
    ]