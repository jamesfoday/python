# Exercise_1.3.py

recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time in minutes: "))
    ingredients = input("Enter ingredients separated by commas: ").split(",")
    ingredients = [ing.strip() for ing in ingredients]  # Clean whitespace
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    return recipe

def main():
    n = int(input("How many recipes would you like to enter? "))
    
    for _ in range(n):
        recipe = take_recipe()
        
        for ingredient in recipe['ingredients']:
            if ingredient not in ingredients_list:
                ingredients_list.append(ingredient)
                
        recipes_list.append(recipe)

    print("\nRecipe Details:\n")
    for recipe in recipes_list:
        cooking_time = recipe['cooking_time']
        num_ingredients = len(recipe['ingredients'])

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

    ingredients_list.sort()
    print("\nAll ingredients encountered (sorted):")
    for ingredient in ingredients_list:
        print(ingredient)

if __name__ == "__main__":
    main()
