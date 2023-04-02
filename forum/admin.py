from django.contrib import admin
from forum.models import *

admin.site.register(FUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(PostRating)
admin.site.register(CommentLike)

