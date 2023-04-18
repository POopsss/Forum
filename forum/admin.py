from django.contrib import admin
from forum.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    def category_m2m(self, post):
        groups = []
        for group in post.category.all():
            groups.append(group.category)
        return ', '.join(groups)
    category_m2m.short_description = 'Category'

    list_display = (
        'author', 'title', 'data', 'category_m2m',
    )


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = (
        'author', 'post', 'data'
    )


@admin.register(FUser)
class FUserAdmin(admin.ModelAdmin):

    def email_fk(self, fuser):
        print(fuser.email.email)
        email = fuser.email.email
        return email
    email_fk.short_description = 'Email'
    list_display = (
        'name', 'email_fk',
    )


# admin.site.register(FUser)
# admin.site.register(Post)
# admin.site.register(Response)
admin.site.register(Category)
admin.site.register(PostCategory)
