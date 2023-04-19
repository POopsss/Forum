from django import template
from django.utils.html import strip_tags

register = template.Library()



# @register.filter()
# def no_img(value):
#     for i in range(len(value)):
#         if value[i:i+10] == '<img src="':
#             for n in range(len(value)):
#                 if value[n:n+2] == '">':
#                     value = value[:i] + value[n+2:]
#                     break
#     return value
