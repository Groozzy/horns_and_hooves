from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from orders import enums
from products.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        User,
        models.CASCADE,
        related_name='orders',
        verbose_name='Пользователь'
    )
    total = models.DecimalField(
        'Итоговая стоимость',
        max_digits=enums.OrderEnums.TOTAL_MAX_DIGITS.value,
        decimal_places=enums.OrderEnums.TOTAL_DECIMAL_PLACES.value
    )


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        models.CASCADE,
        related_name='added_in_orders',
        verbose_name='Продукт'
    )
    order = models.ForeignKey(
        Order,
        models.CASCADE,
        related_name='items',
        verbose_name='Заказ'
    )
    quantity = models.PositiveSmallIntegerField(
        'Количество',
        default=enums.OrderEnums.AMOUNT_DEFAULT_VALUE.value,
        validators=(
            validators.MinValueValidator(
                enums.OrderEnums.AMOUNT_MIN_VALUE,
                'Укажите количество!'
            ),
            validators.MaxValueValidator(
                enums.OrderEnums.AMOUNT_MAX_VALUE,
                'Заказ не резиновый!'
            ),
        )
    )

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'
        ordering = ('order', 'product')
        constraints = (
            models.UniqueConstraint(
                fields=('order', 'product'),
                name='unique_products_in_order_constraint',
            ),
        )

    def __str__(self):
        return (f'Продукт "{self.product.title}" в количестве'
                f' {self.quantity} {self.product.measurement_unit}'
                f' по цене {self.product.price}'
                f' р/{self.product.measurement_unit}')
