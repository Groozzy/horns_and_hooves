from django.contrib import admin

from carts import models


class CartInline(admin.TabularInline):
    model = models.CartItem
    extra = 1


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    inlines = (CartInline,)
