from django.shortcuts import render, redirect
from .models import Book, Author


# =========================
# Books Views
# =========================

# Display all books and show the form to create a new book
def books(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, "books.html", context)


# Create a new book using data from the form
def create_book(request):
    Book.objects.create(
        title=request.POST["title"],
        desc=request.POST["desc"]
    )

    # After creating the book, go back to books page
    return redirect("/books")


# Display one specific book and its authors
def show_book(request, book_id):
    # Get the selected book by id
    book = Book.objects.get(id=book_id)

    context = {
        "book": book,

        # Sensei Bonus:
        # Show only authors that are not already connected to this book
        "available_authors": Author.objects.exclude(books=book)
    }

    return render(request, "show_book.html", context)


# Add an author to a specific book
def add_author_to_book(request, book_id):
    # Get the book from the URL id
    book = Book.objects.get(id=book_id)

    # Get the author selected from the dropdown
    author = Author.objects.get(id=request.POST["author_id"])

    # Add the author to the book
    # Because related_name="authors", we can use book.authors.add()
    book.authors.add(author)

    return redirect(f"/books/{book_id}")


# =========================
# Authors Views
# =========================

# Display all authors and show the form to create a new author
def authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, "authors.html", context)


# Create a new author using data from the form
def create_author(request):
    Author.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        notes=request.POST["notes"]
    )

    # After creating the author, go back to authors page
    return redirect("/authors")


# Display one specific author and their books
def show_author(request, author_id):
    # Get the selected author by id
    author = Author.objects.get(id=author_id)

    context = {
        "author": author,

        # Sensei Bonus:
        # Show only books that are not already connected to this author
        "available_books": Book.objects.exclude(authors=author)
    }

    return render(request, "show_author.html", context)


# Add a book to a specific author
def add_book_to_author(request, author_id):
    # Get the author from the URL id
    author = Author.objects.get(id=author_id)

    # Get the book selected from the dropdown
    book = Book.objects.get(id=request.POST["book_id"])

    # Add the book to the author
    author.books.add(book)

    return redirect(f"/authors/{author_id}")