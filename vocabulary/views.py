from django.shortcuts import render, redirect
from books.models import Flashcard
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
import random

@login_required
def flashcard_list(request):
    flashcards = Flashcard.objects.filter(user=request.user)
    return render(request, 'vocabulary/flashcard_list.html', {'flashcards': flashcards})

@login_required
def add_flashcard(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        translation = request.POST.get('translation')
        if word and translation:
            Flashcard.objects.create(user=request.user, word=word, translation=translation)
            return redirect('flashcard_list')
    return render(request, 'vocabulary/add_flashcard.html')

@login_required
def learn_flashcards(request):
    flashcards = Flashcard.objects.filter(user=request.user)
    data = [
        {'word': card.word, 'translation': card.translation}
        for card in flashcards
    ]
    return JsonResponse({'cards': data})

def learn_flashcards_page(request):
    return render(request, 'vocabulary/learn_flashcards.html')

def learn_flashcards_json(request):
    flashcards = Flashcard.objects.filter(user=request.user)
    data = [{'word': f.word, 'translation': f.translation} for f in flashcards]
    return JsonResponse({'cards': data})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # messages.success(request, 'Аккаунт успешно создан! Теперь вы можете войти.')
            login(request, user)
            return redirect('books_list') 
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})