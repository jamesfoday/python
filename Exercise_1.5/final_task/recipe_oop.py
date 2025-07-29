class Recipe:
    all_ingredients = []  # Class variable to keep track of all unique ingredients

    def __init__(self, name):
        self._name = name
        self.ingredients = []
        self._cooking_time = 0
        self._difficulty = None

    # Getter and Setter for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and Setter for cooking_time
    def get_cooking_time(self):
        return self._cooking_time

    def set_cooking_time(self, cooking_time):
        self._cooking_time = cooking_time
        self._difficulty = None  # Reset difficulty since time changed

    # Add ingredients using variable-length arguments
    def add_ingredients(self, *args):
        for ingredient in args:
            if ingredient not in self.ingredients:
                self.ingredients.append(ingredient)
        self.update_all_ingredients()

    # Getter for ingredients
    def get_ingredients(self):
        return self.ingredients

    # Calculate difficulty based on logic
    def calculate_difficulty(self):
        time = self._cooking_time
        num_ingredients = len(self.ingredients)
        if time < 10 and num_ingredients < 4:
            self._difficulty = "Easy"
        elif time < 10 and num_ingredients >= 4:
            self._difficulty = "Medium"
        elif time >= 10 and num_ingredients < 4:
            self._difficulty = "Intermediate"
        else:
            self._difficulty = "Hard"

    # Getter for difficulty (calculate if None)
    def get_difficulty(self):
        if self._difficulty is None:
            self.calculate_difficulty()
        return self._difficulty

    # Search for ingredient in recipe ingredients
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    # Update class variable all_ingredients with unique ingredients
    def update_all_ingredients(self):
        for ing in self.ingredients:
            if ing not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ing)

    # String representation of recipe
    def __str__(self):
        ingredients_str = ", ".join(self.ingredients)
        return (
            f"Recipe: {self._name}\n"
            f"Cooking Time: {self._cooking_time} minutes\n"
            f"Difficulty: {self.get_difficulty()}\n"
            f"Ingredients: {ingredients_str}"
        )

    # Class method to search for recipes containing a specific ingredient
    @staticmethod
    def recipe_search(data, search_term):
        print(f"\nRecipes containing '{search_term}':")
        found = False
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)
                print("-" * 40)
                found = True
        if not found:
            print("No recipes found with this ingredient.")


# -------- Main execution --------

if __name__ == "__main__":
    # Create recipes
    tea = Recipe("Tea")
    tea.add_ingredients("Tea Leaves", "Sugar", "Water")
    tea.set_cooking_time(5)
    print(tea)
    print("-" * 40)

    coffee = Recipe("Coffee")
    coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
    coffee.set_cooking_time(5)
    print(coffee)
    print("-" * 40)

    cake = Recipe("Cake")
    cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
    cake.set_cooking_time(50)
    print(cake)
    print("-" * 40)

    smoothie = Recipe("Banana Smoothie")
    smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
    smoothie.set_cooking_time(5)
    print(smoothie)
    print("-" * 40)

    # List of recipes
    recipes_list = [tea, coffee, cake, smoothie]

    # Search for recipes by ingredients
    for ingredient in ["Water", "Sugar", "Bananas"]:
        Recipe.recipe_search(recipes_list, ingredient)
