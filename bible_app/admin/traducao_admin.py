"""Admin configuration for TraducaoEspecifica model."""
from django.contrib import admin
from django.core.cache import cache
from django.contrib import messages
from ..models.traducao_especifica import TraducaoEspecifica
from ..utils.text_processor import text_processor

class TraducaoEspecificaAdmin(admin.ModelAdmin):
    list_display = ('termo_original', 'traducao', 'preview', 'created_at')
    search_fields = ('termo_original', 'traducao', 'notas')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('termo_original',)
    
    fieldsets = (
        (None, {
            'fields': ('termo_original', 'traducao')
        }),
        ('Informações Adicionais', {
            'fields': ('notas',),
            'classes': ('collapse',)
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    def preview(self, obj):
        """Show how the term will appear with tooltip."""
        try:
            processed = text_processor.processar_tooltips(obj.termo_original)
            return processed
        except Exception as e:
            return f"Erro ao processar preview: {str(e)}"
    preview.short_description = 'Visualização'
    
    def save_model(self, request, obj, form, change):
        """Clear text processor cache when translation is saved."""
        try:
            super().save_model(request, obj, form, change)
            # Limpa o cache do TextProcessor
            cache.delete('traducoes_especificas_cache')
            messages.success(request, 'Tradução salva com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao salvar tradução: {str(e)}')
    
    class Media:
        css = {
            'all': ('css/tooltip.css',)
        }