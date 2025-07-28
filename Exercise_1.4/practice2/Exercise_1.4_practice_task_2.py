import pickle

def create_recipe():
    # Create the recipe dictionary as described
    recipe = {
        'name': 'Tea',
        'ingredients': ['Tea leaves', 'Water', 'Sugar'],
        'cooking_time': 5,
        'difficulty': 'Easy'
    }
    return recipe

def save_recipe(recipe, filename):
    # Write the recipe dictionary to a binary file using pickle
    with open(filename, 'wb') as file:
        pickle.dump(recipe, file)
    print(f"Recipe saved to {filename}")

def load_recipe(filename):
    # Load the recipe dictionary back from the binary file
    with open(filename, 'rb') as file:
        recipe = pickle.load(file)
    return recipe

def print_recipe(recipe):
    # Nicely format and print the recipe details
    print("\nLoaded Recipe Details:")
    print(f"Name: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {recipe['difficulty']}")

def main():
    filename = "recipe_binary.bin"
    
    # Step 1-2: Create recipe
    recipe = create_recipe()
    
    # Step 3: Save recipe to binary file
    save_recipe(recipe, filename)
    
    # Step 4: Load recipe from binary file
    loaded_recipe = load_recipe(filename)
    
    # Step 4: Print recipe
    print_recipe(loaded_recipe)

if __name__ == "__main__":
    main()
