from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from categories import models


@admin.register(models.Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('indented_title',)
    list_display_links = ('indented_title',)
