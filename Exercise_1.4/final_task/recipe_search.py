import pickle

def display_recipe(recipe):
    print("\nRecipe Name:", recipe['name'])
    print("Cooking Time (minutes):", recipe['cooking_time'])
    print("Ingredients:", ", ".join(recipe['ingredients']))
    print("Difficulty:", recipe['difficulty'])

def search_ingredient(data):
    ingredients = data.get('all_ingredients', [])
    if not ingredients:
        print("No ingredients found in data.")
        return

    # Use 1-based indexing for user-friendly numbering
    print("Available ingredients:")
    for idx, ingredient in enumerate(ingredients, start=1):
        print(f"{idx}. {ingredient}")

    try:
        choice = int(input("Enter the number corresponding to the ingredient you want to search: "))
        if choice < 1 or choice > len(ingredients):
            print("Selection out of range. Please select a valid number.")
            return
        ingredient_searched = ingredients[choice - 1]
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    print(f"\nRecipes containing '{ingredient_searched}':")
    found = False
    for recipe in data.get('recipes_list', []):
        if ingredient_searched in recipe['ingredients']:
            display_recipe(recipe)
            found = True
    if not found:
        print("No recipes found with that ingredient.")

def main():
    filename = input("Enter the binary filename containing recipes: ").strip()

    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        search_ingredient(data)

if __name__ == "__main__":
    main()
