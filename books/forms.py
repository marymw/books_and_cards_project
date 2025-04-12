from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['word', 'translation']

    def clean_word(self):
        word = self.cleaned_data.get('word')
        if not word:
            raise forms.ValidationError("Поле 'Слово' не может быть пустым.")
        return word

    def clean_translation(self):
        translation = self.cleaned_data.get('translation')
        if not translation:
            raise forms.ValidationError("Поле 'Перевод' не может быть пустым.")
        return translation