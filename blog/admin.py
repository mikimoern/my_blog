from django.contrib import admin
from .models import Topic, Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "is_published",
        "topics",
        "author",
        "created_at",
        "update_at",
    ]
    list_display_links = ["id", "title"]
    list_editable = ["is_published"]
    list_filter = ["is_published", "topics"]


admin.site.register(Topic)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
