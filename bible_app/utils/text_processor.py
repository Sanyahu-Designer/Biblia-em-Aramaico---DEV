"""Utility for processing text and adding tooltips."""
import re
from typing import Dict
from django.utils.html import escape
from django.core.cache import cache
from ..models.traducao_especifica import TraducaoEspecifica

class TextProcessor:
    def __init__(self):
        self._cache_key = 'traducoes_especificas_cache'
        self._cache_timeout = 3600  # 1 hora

    @property
    def traducoes(self) -> Dict[str, str]:
        """Get translations dictionary with cache."""
        cached_data = cache.get(self._cache_key)
        
        if cached_data is None:
            try:
                cached_data = {
                    t.termo_original.lower(): t.traducao 
                    for t in TraducaoEspecifica.objects.all()
                }
                cache.set(self._cache_key, cached_data, self._cache_timeout)
            except Exception as e:
                # Fallback em caso de erro
                cached_data = {}
        
        return cached_data

    def processar_tooltips(self, texto: str) -> str:
        """Process text and add tooltips for known translations.
        
        Args:
            texto: Original text to process
            
        Returns:
            str: Processed text with tooltip spans
        """
        if not texto:
            return texto

        try:
            # Escape HTML first
            texto = escape(texto)
            
            # Split text into words while preserving spaces and punctuation
            palavras = re.findall(r'\S+|\s+', texto)
            resultado = []
            
            for palavra in palavras:
                if palavra.isspace():
                    resultado.append(palavra)
                    continue
                    
                termo_limpo = palavra.strip('.,!?:;').lower()
                
                if termo_limpo in self.traducoes:
                    traducao = self.traducoes[termo_limpo]
                    resultado.append(
                        f'<span class="tooltip-word" data-tooltip="{escape(traducao)}">{palavra}</span>'
                    )
                else:
                    resultado.append(palavra)
            
            return ''.join(resultado)
        except Exception as e:
            # Em caso de erro, retorna o texto original sem processamento
            return texto

text_processor = TextProcessor()