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

    print("Available ingredients:")
    for idx, ingredient in enumerate(ingredients):
        print(f"{idx}: {ingredient}")

    try:
        choice = int(input("Enter the number corresponding to the ingredient you want to search: "))
        ingredient_searched = ingredients[choice]
    except (ValueError, IndexError):
        print("Invalid input! Please enter a valid number from the list.")
        return
    else:
        print(f"\nRecipes containing '{ingredient_searched}':")
        found = False
        for recipe in data.get('recipes_list', []):
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)
                found = True
        if not found:
            print("No recipes found with that ingredient.")

def main():
    filename = input("Enter the binary filename containing recipes: ")

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
