from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name="Заголовок")
    slug = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name="URL")
    body = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to="blog/%Y/%m", verbose_name="Изображение")
    date_published = models.DateField(auto_now_add=True, verbose_name="Дата публикации")
    is_published = models.BooleanField(default=True, verbose_name="Признак публикации")
    count_views = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись в блоге"
        verbose_name_plural = "Записи в блоге"
        ordering = ['date_published']
