from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter, Filter
from .models import Post, Category
from django.forms import DateTimeInput
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy


class PostFilter(FilterSet):
    # title = Post(
    #     field_name='title',
    #     lookup_expr='icontains',
    #     label=pgettext_lazy('Поиск в названии статьи', 'Search in the title'),
    # )

    category = ModelMultipleChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label=pgettext_lazy('Категории', 'Category'),
        conjoined=True,
    )

    added_after = DateTimeFilter(
        field_name='data',
        lookup_expr='gt',
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        label=pgettext_lazy('Опубликовано после', 'Published after'),
    )