from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return f"{self.name} - {self.description}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    preview_image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='Изображение (превью)')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Категория')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Владелец')
    is_published = models.BooleanField(default=False, verbose_name='Признак публикации')

    def __str__(self):
        return f"{self.name} - {self.description}\nЦена: {self.price}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']
        permissions = [('can_change_is_published', 'Can change is_published'),
                       ('can_change_description', 'Can change description'),
                       ('can_change_category', 'Can change category')]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number = models.IntegerField(verbose_name='Версия продукта')
    name = models.CharField(max_length=100, verbose_name='Название версии')
    is_current = models.BooleanField(default=True, verbose_name='Актуальность версии')

    def __str__(self):
        return f"{self.name}: {self.number}"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
