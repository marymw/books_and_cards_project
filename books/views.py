from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Card
from .forms import CardForm

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

def read_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # words = book.content.split()
    return render(request, 'books/read_book.html', {'book': book})