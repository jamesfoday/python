# Exercise_1.3.py

recipes_list = []
ingredients_list = []

def take_recipe():
    """
    Collects recipe details from user input and returns a dictionary.
    """
    name = input("Enter recipe name: ").strip()
    
    # Validate cooking_time input
    while True:
        try:
            cooking_time = int(input("Enter cooking time in minutes: ").strip())
            if cooking_time < 0:
                print("Cooking time must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for cooking time.")
    
    # Collect and clean ingredients list
    ingredients_input = input("Enter ingredients separated by commas: ").strip()
    ingredients = [ing.strip() for ing in ingredients_input.split(",") if ing.strip()]
    
    return {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}

def main():
    # Validate number of recipes input
    while True:
        try:
            n = int(input("How many recipes would you like to enter? ").strip())
            if n <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    for _ in range(n):
        recipe = take_recipe()
        
        # Add new ingredients while preserving order and avoiding duplicates
        for ingredient in recipe['ingredients']:
            if ingredient not in ingredients_list:
                ingredients_list.append(ingredient)
        
        recipes_list.append(recipe)

    print("\nRecipe Details:\n")
    for recipe in recipes_list:
        cooking_time = recipe['cooking_time']
        num_ingredients = len(recipe['ingredients'])

        # Calculate difficulty based on cooking time and number of ingredients
        if cooking_time < 10 and num_ingredients < 4:
            difficulty = "Easy"
        elif cooking_time < 10 and num_ingredients >= 4:
            difficulty = "Medium"
        elif cooking_time >= 10 and num_ingredients < 4:
            difficulty = "Intermediate"
        else:
            difficulty = "Hard"

        print(f"Recipe: {recipe['name']}")
        print(f"Cooking Time (minutes): {cooking_time}")
        print(f"Ingredients: {recipe['ingredients']}")
        print(f"Difficulty: {difficulty}")
        print("-" * 30)

    # Sort ingredients list without modifying the original list in-place
    sorted_ingredients_list = sorted(ingredients_list)
    
    print("\nAll ingredients encountered (sorted):")
    for ingredient in sorted_ingredients_list:
        print(ingredient)

if __name__ == "__main__":
    main()
