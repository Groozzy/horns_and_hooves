from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from carts import enums
from products.models import Product

User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(
        User,
        models.CASCADE,
        related_name='cart',
        verbose_name='Пользователь'
    )
    total = models.DecimalField(
        'Итоговая стоимость',
        default=enums.CartEnums.TOTAL_DEFAULT_VALUE.value,
        max_digits=enums.CartEnums.TOTAL_MAX_DIGITS.value,
        decimal_places=enums.CartEnums.TOTAL_DECIMAL_PLACES.value
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ('user',)

    def __str__(self):
        return f'Корзина пользователя "{self.user}"'


class CartItem(models.Model):
    product = models.ForeignKey(
        Product,
        models.CASCADE,
        related_name='added_in_carts',
        verbose_name='Продукт'
    )
    cart = models.ForeignKey(
        Cart,
        models.CASCADE,
        related_name='items',
        verbose_name='Корзина'
    )
    quantity = models.PositiveSmallIntegerField(
        'Количество',
        default=enums.CartEnums.AMOUNT_DEFAULT_VALUE.value,
        validators=(
            validators.MinValueValidator(
                enums.CartEnums.AMOUNT_MIN_VALUE,
                'Укажите количество!'
            ),
            validators.MaxValueValidator(
                enums.CartEnums.AMOUNT_MAX_VALUE,
                'Корзина не резиновая!'
            ),
        )
    )

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'
        ordering = ('cart', 'product')
        constraints = (
            models.UniqueConstraint(
                fields=('cart', 'product'),
                name='unique_products_in_cart_constraint',
            ),
        )

    def __str__(self):
        return (f'Продукт "{self.product.title}" в количестве'
                f' {self.quantity} {self.product.measurement_unit}'
                f' по цене {self.product.price}'
                f' р/{self.product.measurement_unit}')
