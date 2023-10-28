import django_filters
from apps.category.models import Category

class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Category
        fields = ['name', 'data_cadastro', 'data_update',]
        