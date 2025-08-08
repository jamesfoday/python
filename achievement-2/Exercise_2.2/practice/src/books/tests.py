from django.test import TestCase
from decimal import Decimal
from .models import Book

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Book instance for testing
        Book.objects.create(
            name="Test Book",
            genre="Fantasy",
            book_type="hardcover",
            price=Decimal('19.99')  # Use Decimal here for price
        )

    def test_name_field_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_genre_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('genre').max_length
        self.assertEqual(max_length, 100)

    def test_book_type_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('book_type').max_length
        self.assertEqual(max_length, 50)

    def test_price_field(self):
        book = Book.objects.get(id=1)
        price = book.price
        self.assertEqual(price, Decimal('19.99'))  # Compare with Decimal

    def test_str_method(self):
        book = Book.objects.get(id=1)
        self.assertEqual(str(book), "Test Book")
