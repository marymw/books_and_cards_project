from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list, name='books_list'),
    path('<int:book_id>/read/', views.read_book, name='read_book'),
    path('cards/', views.cards_list, name='cards_list'),
    path('cards/add/', views.add_card, name='add_card'),
]