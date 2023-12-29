from django.contrib import admin

from orders import models


class OrderInline(admin.TabularInline):
    model = models.OrderItem
    extra = 1


@admin.register(models.Order)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    inlines = (OrderInline,)
