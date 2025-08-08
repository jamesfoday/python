from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    book_type = models.CharField(max_length=50)  # e.g., hardcover, eBook
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name
