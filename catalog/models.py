from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}. {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    price = models.IntegerField(verbose_name='Цена за покупку', default=0)
    created_at = models.DateField(verbose_name='Дата создания', blank=True, null=True)
    updated_at = models.DateField(verbose_name='Дата последнего изменения', blank=True, null=True)

    def __str__(self):
        return f'{self.name}. {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category', 'price']

