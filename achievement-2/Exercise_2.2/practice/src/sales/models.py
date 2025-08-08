from django.db import models
from books.models import Book  # Assuming you have a books app with Book model
from customer.models import Customer  # Assuming a customers app

class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sale_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.book.name} sold to {self.customer.name}"
