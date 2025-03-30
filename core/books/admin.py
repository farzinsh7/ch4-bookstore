from django.contrib import admin
from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review
    
    
class BookAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    list_display = ("title", "author", "price",)
    search_fields = ("title", "author")

    
# Register your models here.
admin.site.register(Book, BookAdmin)