class Recipe:
    all_ingredients = set()  # Class variable to track all unique ingredients

    def __init__(self, name):
        self._name = name
        self._ingredients = set()
        self._cooking_time = 0
        self._difficulty = None

    # Property for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Property for cooking_time
    @property
    def cooking_time(self):
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, value):
        self._cooking_time = value
        self._difficulty = None  # Reset difficulty to force recalculation

    # Property for ingredients
    @property
    def ingredients(self):
        return list(self._ingredients)

    @ingredients.setter
    def ingredients(self, new_ingredients):
        self._ingredients = set(new_ingredients)
        self._difficulty = None  # Reset difficulty
        self.update_all_ingredients()

    def add_ingredients(self, *args):
        self._ingredients.update(args)
        self._difficulty = None
        self.update_all_ingredients()

    # Calculate difficulty based on cooking time and number of ingredients
    def calculate_difficulty(self):
        count = len(self._ingredients)
        time = self._cooking_time
        if time < 10 and count < 4:
            self._difficulty = "Easy"
        elif time < 10 and count >= 4:
            self._difficulty = "Medium"
        elif time >= 10 and count < 4:
            self._difficulty = "Intermediate"
        else:
            self._difficulty = "Hard"

    # Property for difficulty (calculated on demand)
    @property
    def difficulty(self):
        if self._difficulty is None:
            self.calculate_difficulty()
        return self._difficulty

    # Update class variable all_ingredients
    def update_all_ingredients(self):
        Recipe.all_ingredients.update(self._ingredients)

    # Check if ingredient is in recipe
    def search_ingredient(self, ingredient):
        return ingredient in self._ingredients

    def __str__(self):
        ingredients_str = ", ".join(sorted(self._ingredients))
        return (
            f"Recipe: {self._name}\n"
            f"Cooking Time: {self._cooking_time} minutes\n"
            f"Difficulty: {self.difficulty}\n"
            f"Ingredients: {ingredients_str}"
        )

    @staticmethod
    def recipe_search(recipes, search_term):
        print(f"\nRecipes containing '{search_term}':")
        found = False
        for recipe in recipes:
            if recipe.search_ingredient(search_term):
                print(recipe)
                print("-" * 40)
                found = True
        if not found:
            print("No recipes found with this ingredient.")


# -------- Main execution --------

if __name__ == "__main__":
    tea = Recipe("Tea")
    tea.add_ingredients("Tea Leaves", "Sugar", "Water")
    tea.cooking_time = 5
    print(tea)
    print("-" * 40)

    coffee = Recipe("Coffee")
    coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
    coffee.cooking_time = 5
    print(coffee)
    print("-" * 40)

    cake = Recipe("Cake")
    cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
    cake.cooking_time = 50
    print(cake)
    print("-" * 40)

    smoothie = Recipe("Banana Smoothie")
    smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
    smoothie.cooking_time = 5
    print(smoothie)
    print("-" * 40)

    recipes_list = [tea, coffee, cake, smoothie]

    for ingredient in ["Water", "Sugar", "Bananas"]:
        Recipe.recipe_search(recipes_list, ingredient)
