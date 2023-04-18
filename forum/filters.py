from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter, Filter, CharFilter
from .models import Category
from django.forms import DateTimeInput


class PostFilter(FilterSet):
    title = Filter(
        field_name='title',
        lookup_expr='icontains',
        label='Поиск в названии статьи',
    )

    category = ModelMultipleChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Категории',
        conjoined=True,
    )

    added_after = DateTimeFilter(
        field_name='date',
        lookup_expr='gt',
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Опубликовано после',
    )


class ResponseFilter(FilterSet):
    author = CharFilter(
        field_name='author__name',
        lookup_expr='icontains',
        label='От кого',
    )

    post = Filter(
        field_name='post__title',
        lookup_expr='icontains',
        label='Объявление',
    )

    added_after = DateTimeFilter(
        field_name='date',
        lookup_expr='gt',
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Опубликовано после',
    )
