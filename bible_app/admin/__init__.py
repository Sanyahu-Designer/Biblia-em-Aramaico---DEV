"""Admin configuration for the Bible app."""
from django.contrib import admin
from ..models import Book, Chapter, Verse
from .book_admin import BookAdmin
from .chapter_admin import ChapterAdmin
from .verse_admin import VerseAdmin

# Register models with their custom admin classes
admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Verse, VerseAdmin)