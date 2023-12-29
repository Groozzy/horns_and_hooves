from django.core import validators
from django.db import models

from categories.models import Category
from products import enums


class Brand(models.Model):
    logo = models.ImageField('Логотип', upload_to='brand_logos/')
    title = models.CharField(
        'Название',
        max_length=enums.BrandEnums.TITLE_MAX_LEN.value,
        validators=(
            validators.MinLengthValidator(
                enums.BrandEnums.TITLE_MIN_LEN.value,
                'Название бренда слишком короткое'
            ),
        )
    )
    description = models.TextField(
        'Описание',
        max_length=enums.BrandEnums.DESCRIPTION_MAX_LEN.value
    )

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ('title',)
        constraints = (
            models.UniqueConstraint(
                fields=('title',),
                name='brand_duplication_constraint',
            ),
        )

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(
        'Название',
        max_length=enums.ProductEnums.TITLE_MAX_LEN.value,
        validators=(
            validators.MinLengthValidator(
                enums.ProductEnums.TITLE_MIN_LEN.value,
                'Название продукта слишком короткое'
            ),
        )
    )
    image = models.ImageField('Изображение', upload_to='product_images/')
    description = models.TextField(
        'Описание',
        max_length=enums.ProductEnums.DESCRIPTION_MAX_LEN.value
    )
    price = models.DecimalField(
        'Цена',
        max_digits=enums.ProductEnums.PRICE_MAX_DIGITS.value,
        decimal_places=enums.ProductEnums.PRICE_DECIMAL_PLACES.value,
    )
    measurement_unit = models.CharField(
        'Единица измерения',
        max_length=enums.ProductEnums.MEASUREMENT_UNIT_MAX_LEN.value
    )
    brand = models.ForeignKey(
        Brand,
        models.CASCADE,
        related_name='products',
        verbose_name='Бренд',
    )
    categories = models.ManyToManyField(
        Category,
        related_name='products',
        verbose_name='Категории',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('title', 'brand')
        constraints = (
            models.UniqueConstraint(
                fields=('title', 'brand'),
                name='product_duplication_constraint',
            ),
        )

    def __str__(self):
        return f'Продукт "{self.title}" бренда "{self.brand}"'
