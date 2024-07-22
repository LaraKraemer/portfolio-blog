from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ("author", "title", "created_date", "published_date")
    list_filter = ("created_date",)
    search_fields = ("created_date", "published_date")
    summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)
