from django.contrib import admin
from apps.posts.models import Post


@admin.register(Post)
class LikeNewsAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
