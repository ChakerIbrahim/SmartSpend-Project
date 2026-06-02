from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(default="")
    
    # Many-to-Many relationship between authors and books
    books = models.ManyToManyField(Book, related_name="authors")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
