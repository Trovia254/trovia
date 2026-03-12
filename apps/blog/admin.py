from django.contrib import admin
from .models import Post, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "category", "status", "published_at"]
    list_filter = ["status", "category", "published_at"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"
    ordering = ["-published_at"]
