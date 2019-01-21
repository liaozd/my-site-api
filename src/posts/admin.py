from django.contrib import admin

from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'update', 'timestamp']
    list_display_links = ['update', 'timestamp']
    list_filter = ['update', 'timestamp']
    list_editable = ['title']
    search_fields = ['title']

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
