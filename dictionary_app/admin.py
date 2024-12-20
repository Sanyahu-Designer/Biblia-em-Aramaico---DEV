from django.contrib import admin
from .models import AramaicWord

@admin.register(AramaicWord)
class AramaicWordAdmin(admin.ModelAdmin):
    list_display = ('aramaic_word', 'transliteration', 'portuguese_translation')
    search_fields = ('aramaic_word', 'transliteration', 'portuguese_translation')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
