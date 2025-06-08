from django.db import models

class BlogEntry(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Заголовок",
        help_text="Введите заголовок записи в блоге",
    )
    content = models.TextField(
        verbose_name="Содержимое записи",
        help_text="Введите содержимое записи в блоге",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="blog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение для записи блога",
    )

    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата будет установлена автоматически при создании записи",
    )

    viewed = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Введите количество просмотров записи в блоге",
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name="Флаг публикации записи",
        help_text="Укажите, опубликована ли запись",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись в блоге"
        verbose_name_plural = "Записи в блоге"
