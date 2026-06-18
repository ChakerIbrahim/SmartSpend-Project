from django.urls import path
from . import views

urlpatterns = [
    # Books routes
    path('', views.books),
    path('books', views.books),
    path('books/create', views.create_book),
    path('books/<int:book_id>', views.show_book),
    path('books/<int:book_id>/add_author', views.add_author_to_book),

    # Authors routes
    path('authors', views.authors),
    path('authors/create', views.create_author),
    path('authors/<int:author_id>', views.show_author),
    path('authors/<int:author_id>/add_book', views.add_book_to_author),
]
