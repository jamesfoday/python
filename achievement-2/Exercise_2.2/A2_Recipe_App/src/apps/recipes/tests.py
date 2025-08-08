from django.test import TestCase
from .models import Recipe, RecipeIngredient
from ingredients.models import Ingredient

class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.recipe = Recipe.objects.create(
            name="Chocolate Cake",
            cooking_time=45,
            description="Delicious chocolate cake recipe."
        )

    def test_name_field_label(self):
        field_label = self.recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_cooking_time_help_text(self):
        help_text = self.recipe._meta.get_field('cooking_time').help_text
        self.assertEqual(help_text, 'Cooking time in minutes')

    def test_str_method(self):
        self.assertEqual(str(self.recipe), "Chocolate Cake")

class RecipeIngredientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.ingredient = Ingredient.objects.create(name="Flour")
        cls.recipe = Recipe.objects.create(
            name="Pancakes",
            cooking_time=20,
            description="Simple pancake recipe."
        )
        cls.recipe_ingredient = RecipeIngredient.objects.create(
            recipe=cls.recipe,
            ingredient=cls.ingredient,
            quantity="2 cups"
        )

    def test_quantity_max_length(self):
        max_length = self.recipe_ingredient._meta.get_field('quantity').max_length
        self.assertEqual(max_length, 50)

    def test_str_method(self):
        expected_str = "2 cups of Flour for Pancakes"
        self.assertEqual(str(self.recipe_ingredient), expected_str)

    def test_recipe_relation(self):
        self.assertEqual(self.recipe_ingredient.recipe.name, "Pancakes")

    def test_ingredient_relation(self):
        self.assertEqual(self.recipe_ingredient.ingredient.name, "Flour")
