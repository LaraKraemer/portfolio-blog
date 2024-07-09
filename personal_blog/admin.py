from django.contrib import admin
from .models import Post

class BlogAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "created_date", "published_date")
    list_filter = ("created_date",)
    search_fields = ("created_date", "published_date")
admin.site.register(Post, BlogAdmin)
