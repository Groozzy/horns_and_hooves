from django_filters.rest_framework import FilterSet, filters

from products.models import Product, Brand


class ProductFilter(FilterSet):
    category = filters.AllValuesMultipleFilter(field_name='category__slug')
    brand = filters.ModelChoiceFilter(queryset=Brand.objects.all())

    class Meta:
        model = Product
        fields = ('brand', 'category')
