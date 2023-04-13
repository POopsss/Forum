from django.contrib import admin
from forum.models import *

admin.site.register(FUser)
admin.site.register(Post)
admin.site.register(Response)
admin.site.register(Category)
admin.site.register(PostCategory)
