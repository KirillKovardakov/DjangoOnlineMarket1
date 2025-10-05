from django.db import models


# Create your models here.
class Blog(models.Model):
    headline = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое', blank=True, null=True)
    preview = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='Превью')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name='Признак публикации')
    count_views = models.IntegerField(default=0,verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.headline}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['headline', 'count_views', 'is_published']