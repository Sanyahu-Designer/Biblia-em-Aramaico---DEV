"""Model for Bible verses with automatic tooltip processing."""
from django.db import models
from django.core.cache import cache
from ..utils.text_processor import text_processor

class Verse(models.Model):
    TRANSLATOR_CHOICES = [
        ('yosef_chaim', 'Yosef Chaim'),
        ('netzer_netzarim', 'Netzer Netzarim'),
    ]

    ARAMAIC_SOURCE_CHOICES = [
        ('curetonian', 'Antigos Evangelhos Curetonianos Siríacos'),
        ('sinaiticus', 'Palimpsesto Sinaítico Siríaco Antigo'),
        ('peshitta', 'Peshitta'),
    ]

    chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE, related_name='verses')
    number = models.IntegerField('Número do Versículo')
    aramaic_text = models.TextField('Texto em Aramaico')
    portuguese_text = models.TextField('Texto em Português')
    translator_note = models.TextField('Nota do Tradutor', blank=True, null=True)
    translator = models.CharField('Tradutor', max_length=20, choices=TRANSLATOR_CHOICES)
    aramaic_source = models.CharField('Fonte do Texto Aramaico', max_length=20, choices=ARAMAIC_SOURCE_CHOICES)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ['number']
        verbose_name = 'Versículo'
        verbose_name_plural = 'Versículos'
        unique_together = ['chapter', 'number']

    def __str__(self):
        return f"{self.chapter.book.name} {self.chapter.number}:{self.number}"

    @property
    def processed_portuguese_text(self):
        """Get text with tooltips processed on demand."""
        cache_key = f'verse_processed_text_{self.id}_{self.updated_at.timestamp()}'
        cached_text = cache.get(cache_key)
        
        if cached_text is None:
            try:
                cached_text = text_processor.processar_tooltips(self.portuguese_text)
                cache.set(cache_key, cached_text, 3600)  # Cache por 1 hora
            except Exception as e:
                # Em caso de erro, retorna o texto original sem processamento
                cached_text = self.portuguese_text
        
        return cached_text

    def save(self, *args, **kwargs):
        """Override save to clear cache when verse is updated."""
        # Limpa o cache do texto processado
        cache_key = f'verse_processed_text_{self.id}_{self.updated_at.timestamp()}'
        cache.delete(cache_key)
        
        super().save(*args, **kwargs)