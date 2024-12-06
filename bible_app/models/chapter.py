"""Model for Bible chapters."""
from django.db import models

class Chapter(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='chapters')
    number = models.IntegerField('Número do Capítulo')
    
    class Meta:
        ordering = ['number']
        verbose_name = 'Capítulo'
        verbose_name_plural = 'Capítulos'
        unique_together = ['book', 'number']
    
    def __str__(self):
        return f"{self.book.name} - Capítulo {self.number}"