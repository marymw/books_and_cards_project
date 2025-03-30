from django.db import models
from books.models import Book  

class Word(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='words')
    original = models.CharField("Оригинал", max_length=100)
    translation = models.CharField("Перевод", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original} → {self.translation}"
