from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter, Filter, CharFilter
from .models import Category
from django.forms import DateTimeInput
from django.utils.translation import pgettext_lazy


class PostFilter(FilterSet):
    title = Filter(
        field_name='title',
        lookup_expr='icontains',
        label=pgettext_lazy('Поиск в названии статьи', 'Search in the title'),
    )

    category = ModelMultipleChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label=pgettext_lazy('Категории', 'Category'),
        conjoined=True,
    )

    added_after = DateTimeFilter(
        field_name='date',
        lookup_expr='gt',
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        label=pgettext_lazy('Опубликовано после', 'Published after'),
    )


class ResponseFilter(FilterSet):
    author = CharFilter(
        field_name='author__name',
        lookup_expr='icontains',
        label=pgettext_lazy('От кого', 'From'),
    )

    post = Filter(
        field_name='post__title',
        lookup_expr='icontains',
        label=pgettext_lazy('Объявление', 'Post'),
    )

    added_after = DateTimeFilter(
        field_name='date',
        lookup_expr='gt',
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        label=pgettext_lazy('Опубликовано после', 'Published after'),
    )
