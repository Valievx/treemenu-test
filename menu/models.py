from django.db import models


class Menu(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Url',
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        related_name='child',
        verbose_name='Родитель',
        default=None
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
