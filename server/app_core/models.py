from django.db import models


class Published(models.Model):
    published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        abstract = True


class Localized(models.Model):
    LANG_CHOISES = (
        ("RU", "ru"),
        ("EN", "en"),
    )

    lang = models.CharField(
        max_length=2, choices=LANG_CHOISES, default="RU", verbose_name="Язык"
    )

    class Meta:
        abstract = True
