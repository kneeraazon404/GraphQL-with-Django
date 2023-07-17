from django.contrib import admin

from .models import Books


# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price", "created_at")
    search_fields = ("title", "author")
    list_filter = ("author", "created_at")
    ordering = ("author", "created_at")
    fields = ("title", "author", "price", "description", "image")
    readonly_fields = ("created_at", "updated_at")
    filter_horizontal = ()
    fieldsets = ()
