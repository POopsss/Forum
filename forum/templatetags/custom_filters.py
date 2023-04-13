from django import template
from django.utils.html import strip_tags

register = template.Library()



@register.filter()
def censor(value):
    for i in range(len(value)):
        if value[i:i+10] == '<img src="':
            for n in range(len(value)):
                if value[n:n+2] == '">':
                    value = value[:i] + value[n+2:]
                    break
    # value = strip_tags(value)
    # for i in range(len(value)):
    #     if value[i:i+4] == '</p>':
    #         value = value[:i] + value[i+4:]
    #     if value[i:i+3] == '<p>':
    #         value = value[:i] + value[i+3:]
    # for i in range(len(value)):
    #     if value[i:i+4] == '<br>':
    #         value = value[:i] + value[i+4:]
    return value
