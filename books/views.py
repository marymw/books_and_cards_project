from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Card
from .forms import CardForm
from .models import Flashcard
from django.http import JsonResponse
from googletrans import Translator
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer

def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/list.html', {'books': books})

def book_reader(request, pk):
    book = get_object_or_404(Book, pk=pk)
    words = book.content.split()
    return render(request, 'books/reader.html', {'book': book, 'words': words})

def cards_list(request):
    cards = Card.objects.all()
    return render(request, 'books/cards_list.html', {'cards': cards})

def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cards_list')
    else:
        form = CardForm()
    return render(request, 'books/add_card.html', {'form': form})

# def read_book(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     # words = book.content.split()
#     return render(request, 'books/read_book.html', {'book': book})
def read_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    paragraphs = book.content.split('\n')
    return render(request, 'books/read_book.html', {'book': book, 'paragraphs': paragraphs})


def get_translation(request, word):
    translator = Translator()
    translation = translator.translate(word, src='en', dest='ru')
    return JsonResponse({
        'word': word,
        'translation': translation.text
    })

def add_flashcard(request, word):
    translator = Translator()
    translation = translator.translate(word, src='en', dest='ru').text
    user = request.user

    flashcard, created = Flashcard.objects.get_or_create(
        user=user,
        word=word,
        defaults={'translation': translation}
    )

    if created:
        message = f'Слово "{word}" добавлено в карточки!'
    else:
        message = f'Слово "{word}" уже есть в карточках.'

    return JsonResponse({'message': message})


def translate_word(request, word):
    translator = Translator()
    translation = translator.translate(word, src='en', dest='ru')
    return JsonResponse({'word': word, 'translation': translation.text})

@api_view(['GET'])
def book_list_api(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
