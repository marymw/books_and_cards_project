from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list, name='books_list'),
    path('<int:book_id>/read/', views.read_book, name='read_book'),
    # path('cards/', views.cards_list, name='cards_list'),
    # path('cards/add/', views.add_card, name='add_card'),
    path('translate/<str:word>/', views.get_translation, name='get_translation'),
    path('add_flashcard/<str:word>/', views.add_flashcard, name='add_flashcard'),
    path('api/', views.book_list_api, name='book_list_api'), 
]