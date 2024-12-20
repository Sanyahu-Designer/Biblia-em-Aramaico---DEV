from django.db import models

class AramaicWord(models.Model):
    aramaic_word = models.CharField("Palavra Aramaica", max_length=200)
    transliteration = models.CharField("Transliteração", max_length=200)
    portuguese_translation = models.TextField("Tradução em Português")
    pronunciation_audio = models.FileField("Áudio da Pronúncia", upload_to='audio/', blank=True, null=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Palavra Aramaica"
        verbose_name_plural = "Palavras Aramaicas"
        ordering = ["aramaic_word"]

    def __str__(self):
        return self.aramaic_word
