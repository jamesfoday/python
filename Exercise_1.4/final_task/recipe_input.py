import pickle

def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"

def take_recipe():
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (minutes): "))
    
    ingredients = []
    print("Enter ingredients one by one. Type 'done' when finished:")
    while True:
        ingredient = input("> ")
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)

    difficulty = calc_difficulty(cooking_time, len(ingredients))

    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }
    return recipe

def main():
    filename = input("Enter the binary filename to load/save recipes: ")
    
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Creating new data store.")
        data = {'recipes_list': [], 'all_ingredients': []}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        data = {'recipes_list': [], 'all_ingredients': []}
    else:
        print(f"Loaded data from {filename}")
    finally:
        recipes_list = data.get('recipes_list', [])
        all_ingredients = data.get('all_ingredients', [])

    n = int(input("How many recipes would you like to enter? "))
    for _ in range(n):
        recipe = take_recipe()
        recipes_list.append(recipe)

        for ingredient in recipe['ingredients']:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

    with open(filename, 'wb') as file:
        pickle.dump(data, file)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    main()
