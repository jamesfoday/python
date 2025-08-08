from django.test import TestCase
from .models import Ingredient

class IngredientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.ingredient = Ingredient.objects.create(name="Sugar")

    def test_name_field_label(self):
        field_label = self.ingredient._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        max_length = self.ingredient._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_str_method(self):
        self.assertEqual(str(self.ingredient), "Sugar")
