from django.contrib import admin

from .models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_date', 'published_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_editable = ('published_date',)
    list_filter = ('published_date', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)
