from django.contrib import admin
from links.models import Bookmark

#admin.site.register(Bookmark)

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    # Columns to show in the table
    list_display = ('user', 'title', 'url', 'tag', 'importance_level', 'created_at')
    
    # Sidebar filters on the right
    list_filter = ('user', 'tag')
    
    # Search bar fields
    search_fields = ('title', 'tag')

