from django.db import models
from django.contrib.auth.models import User
class Book(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class Card(models.Model):
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=255)
    added_from_book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.word} - {self.translation}"

class Flashcard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flashcards')
    word = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)

    def str(self):
        return f"{self.word} - {self.translation}"
    