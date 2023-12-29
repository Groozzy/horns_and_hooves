# Generated by Django 5.0 on 2023-12-26 20:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "logo",
                    models.ImageField(upload_to="brand_logos/", verbose_name="Логотип"),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=128,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                2, "Название бренда слишком короткое"
                            )
                        ],
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    models.TextField(max_length=4096, verbose_name="Описание"),
                ),
            ],
            options={
                "verbose_name": "Бренд",
                "verbose_name_plural": "Бренды",
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                2, "Название продукта слишком короткое"
                            )
                        ],
                        verbose_name="Название",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="product_images/", verbose_name="Изображение"
                    ),
                ),
                (
                    "description",
                    models.TextField(max_length=4096, verbose_name="Описание"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Цена"
                    ),
                ),
                (
                    "measurement_unit",
                    models.CharField(max_length=16, verbose_name="Единица измерения"),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
                "ordering": ("title", "brand"),
            },
        ),
        migrations.AddConstraint(
            model_name="brand",
            constraint=models.UniqueConstraint(
                fields=("title",), name="brand_duplication_constraint"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="brand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="products.brand",
                verbose_name="Бренд",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="categories",
            field=models.ManyToManyField(
                related_name="products",
                to="categories.category",
                verbose_name="Категории",
            ),
        ),
        migrations.AddConstraint(
            model_name="product",
            constraint=models.UniqueConstraint(
                fields=("title", "brand"), name="product_duplication_constraint"
            ),
        ),
    ]