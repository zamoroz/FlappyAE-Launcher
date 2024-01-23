from django.db import models

from app_core.models import Localized, Published


class News(Published, Localized):
    title = models.CharField(verbose_name="Заголовок")
    background = models.ImageField(verbose_name="Картинка")
    link = models.CharField(blank=True, verbose_name="Ссылка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Social(Published):
    title = models.CharField(verbose_name="Закголовок")
    icon = models.ImageField(verbose_name="Иконка")
    link = models.CharField(verbose_name="Ссылка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Соцсеть"
        verbose_name_plural = "Социальные сети"


class Update(Published, Localized):
    version = models.CharField(verbose_name="Версия")
    previous = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, verbose_name="Обновление с"
    )
    beta = models.BooleanField(default=False, verbose_name="Для бета-тестеров")
    clean_profiles = models.BooleanField(default=False, verbose_name="Удалить профили")
    clean_inis = models.BooleanField(
        default=True,
        verbose_name="Удалить .ini файлы",
        help_text="Modorganizer.ini, nemesis.ini",
    )
    update_file = models.FileField(
        verbose_name="Файл обновления", help_text="Архив или торрент", null=True
    )
    mods_to_remove = models.TextField(
        blank=True,
        verbose_name="Моды на удаление",
        help_text="Список папок без кавычек и прочей хуйни, через запятую",
    )
    files_to_remove = models.TextField(
        blank=True,
        verbose_name="Файлы на удаление",
        help_text="Если нужно удалить конкретные файлы, правила те же, путь от FlappyRU. Например: mods/мод_на_еблю_с_рыбами/карась.ini, ModOrganiser.ini",
    )

    def __str__(self):
        return f"{self.version} {self.lang}"

    class Meta:
        verbose_name = "Обновление"
        verbose_name_plural = "Обновления"
