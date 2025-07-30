import pickle

def get_recipes():
    recipes = []
    while True:
        try:
            n = int(input("How many recipes would you like to enter? ").strip())
            if n <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for i in range(n):
        print(f"\nEntering details for recipe {i+1}")
        name = input("Enter recipe name: ").strip()
        
        while True:
            try:
                cooking_time = int(input("Enter cooking time in minutes: ").strip())
                if cooking_time < 0:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        ingredients = []
        print("Enter ingredients one by one:")

        for idx in range(n):
            ingredient = input(f"Ingredient {idx+1}: ").strip()
            if ingredient == "":
                print("Ingredient cannot be empty.")
                return
            ingredients.append(ingredient)
        
        recipe = {
            'name': name,
            'cooking_time': cooking_time,
            'ingredients': ingredients
        }
        recipes.append(recipe)
    return recipes

def save_recipes(recipes, filename='my_cook_book.bin'):
    with open(filename, 'wb') as f:
        pickle.dump(recipes, f)
    print(f"Recipes saved successfully to {filename}")

def load_recipes(filename='my_cook_book.bin'):
    try:
        with open(filename, 'rb') as f:
            recipes = pickle.load(f)
        return recipes
    except FileNotFoundError:
        print(f"No saved file named {filename} found.")
        return []

def display_recipes(recipes):
    if not recipes:
        print("No recipes to display.")
        return
    print("\nYour recipes:")
    for idx, recipe in enumerate(recipes, 1):
        print(f"\nRecipe {idx}: {recipe['name']}")
        print(f"Cooking time: {recipe['cooking_time']} minutes")
        print("Ingredients:")
        for ing_idx, ingredient in enumerate(recipe['ingredients'], 1):
            print(f"  {ing_idx}. {ingredient}")

def search_ingredient(recipes):
    all_ingredients = []
    for recipe in recipes:
        for ingredient in recipe['ingredients']:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    all_ingredients.sort()
    print("\nAvailable ingredients:")
    for idx, ingredient in enumerate(all_ingredients, 1):
        print(f"{idx}. {ingredient}")

    try:
        selections = input("Select ingredient numbers separated by spaces: ").strip().split()
        selections = [int(s) for s in selections]
    except ValueError:
        print("Error: Please enter only numbers separated by spaces.")
        return
    
    if any(s < 1 or s > len(all_ingredients) for s in selections):
        print("Error: One or more selections are out of range.")
        return

    search_ingredients = [all_ingredients[s - 1] for s in selections]
    
    print(f"\nRecipes containing: {', '.join(search_ingredients)}")
    found = False
    for recipe in recipes:
        if all(ing in recipe['ingredients'] for ing in search_ingredients):
            print(f"- {recipe['name']}")
            found = True
    if not found:
        print("No recipes found with those ingredients.")

def main():
    recipes = get_recipes()
    save_recipes(recipes)
    loaded_recipes = load_recipes()
    display_recipes(loaded_recipes)
    search_ingredient(loaded_recipes)

if __name__ == "__main__":
    main()
