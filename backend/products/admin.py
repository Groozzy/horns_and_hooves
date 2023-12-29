from django.contrib import admin

from products import models


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'brand', 'added_in_favorites')
    readonly_fields = ('added_in_favorites',)
    list_filter = ('title', 'brand')
    fieldsets = (
        (
            None, {
                'fields': (
                    'title',
                    'brand',
                    'measurement_unit',
                    'price',
                    'categories',
                    'image',
                    'description',
                )
            }
        ),
    )
    filter_horizontal = ('categories',)

    @admin.display(description='Количество добавлений в избранное')
    def added_in_favorites(self, product):
        return product.added_in_favorites.count()
