from django.urls import path
from . import views

urlpatterns = [
    path('', views.flashcard_list, name='flashcard_list'),
    path('add/', views.add_flashcard, name='add_flashcard_manual'),
    # path('learn/', views.learn_flashcards, name='learn_flashcards'),
    path('learn/', views.learn_flashcards_page, name='learn_flashcards_page'),
    path('learn/json/', views.learn_flashcards_json, name='learn_flashcards_json'),
    path('signup/', views.signup, name='signup'),
]
