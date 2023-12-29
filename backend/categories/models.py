from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from categories import enums

User = get_user_model()


class Category(MPTTModel):
    title = models.CharField(
        'Название',
        max_length=enums.CategoryEnums.TITLE_MAX_LEN.value,
        unique=True,
    )
    slug = models.SlugField(
        'Слаг',
        max_length=enums.CategoryEnums.SLUG_MAX_LEN.value,
        unique=True,
        db_index=False,
    )
    parent = TreeForeignKey(
        'self',
        models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('slug',)
        constraints = (
            models.UniqueConstraint(
                fields=('title', 'parent'),
                name='category_duplication_constraint',
            ),
        )

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title
