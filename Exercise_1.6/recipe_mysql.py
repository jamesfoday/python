import mysql.connector

def connect_database():
    # Connect to MySQL Server
    conn = mysql.connector.connect(
        host='localhost',
        user='cf-python',
        passwd='password'
    )
    cursor = conn.cursor()
    
    # Create database and use it
    cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
    cursor.execute("USE task_database")
    
    # Create Recipes table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Recipes (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50),
            ingredients VARCHAR(255),
            cooking_time INT,
            difficulty VARCHAR(20)
        )
    ''')
    return conn, cursor

def calculate_difficulty(cooking_time, ingredients):
    count = len(ingredients)
    if cooking_time < 10 and count < 4:
        return "Easy"
    elif cooking_time < 10 and count >= 4:
        return "Medium"
    elif cooking_time >= 10 and count < 4:
        return "Intermediate"
    else:
        return "Hard"

def create_recipe(conn, cursor):
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (minutes): "))
    ingredients_input = input("Enter ingredients (comma-separated): ")
    ingredients = [i.strip() for i in ingredients_input.split(',')]
    
    difficulty = calculate_difficulty(cooking_time, ingredients)
    ingredients_str = ", ".join(ingredients)
    
    sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    val = (name, ingredients_str, cooking_time, difficulty)
    cursor.execute(sql, val)
    conn.commit()
    print(f"Recipe '{name}' added successfully!")

def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    
    all_ingredients = set()
    for row in results:
        if row[0]:
            ingredients_list = [i.strip() for i in row[0].split(',')]
            all_ingredients.update(ingredients_list)
        
    all_ingredients = sorted(list(all_ingredients))
    if not all_ingredients:
        print("No ingredients found in any recipe.")
        return
    
    print("Available ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")
        
    choice = int(input("Pick an ingredient by number to search recipes: "))
    if choice < 1 or choice > len(all_ingredients):
        print("Invalid choice.")
        return
    search_ingredient = all_ingredients[choice - 1]
    
    query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    pattern = f"%{search_ingredient}%"
    cursor.execute(query, (pattern,))
    results = cursor.fetchall()
    
    if results:
        print(f"Recipes containing '{search_ingredient}':")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Cooking Time: {row[3]} mins, Difficulty: {row[4]}")
            print(f"Ingredients: {row[2]}")
            print("-" * 40)
    else:
        print(f"No recipes found with ingredient '{search_ingredient}'.")

def update_recipe(conn, cursor):
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()
    
    if not recipes:
        print("No recipes available to update.")
        return
    
    print("Recipes:")
    for r in recipes:
        print(f"{r[0]}. {r[1]}")
    
    recipe_id = int(input("Enter the ID of the recipe to update: "))
    
    # Check if recipe exists
    cursor.execute("SELECT id FROM Recipes WHERE id = %s", (recipe_id,))
    if cursor.fetchone() is None:
        print("Recipe with that ID does not exist.")
        return
    
    print("What do you want to update?")
    print("1. Name")
    print("2. Cooking Time")
    print("3. Ingredients")
    choice = int(input("Enter choice (1-3): "))
    
    if choice == 1:
        new_name = input("Enter new recipe name: ")
        sql = "UPDATE Recipes SET name = %s WHERE id = %s"
        cursor.execute(sql, (new_name, recipe_id))
    elif choice == 2:
        new_cooking_time = int(input("Enter new cooking time (minutes): "))
        cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        result = cursor.fetchone()
        if result is None or result[0] is None:
            print("Cannot find ingredients for this recipe.")
            return
        current_ingredients = result[0].split(", ")
        difficulty = calculate_difficulty(new_cooking_time, current_ingredients)
        
        sql = "UPDATE Recipes SET cooking_time = %s, difficulty = %s WHERE id = %s"
        cursor.execute(sql, (new_cooking_time, difficulty, recipe_id))
    elif choice == 3:
        new_ingredients_input = input("Enter new ingredients (comma-separated): ")
        new_ingredients = [i.strip() for i in new_ingredients_input.split(',')]
        cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
        result = cursor.fetchone()
        if result is None or result[0] is None:
            print("Cannot find cooking time for this recipe.")
            return
        current_cooking_time = result[0]
        difficulty = calculate_difficulty(current_cooking_time, new_ingredients)
        ingredients_str = ", ".join(new_ingredients)
        
        sql = "UPDATE Recipes SET ingredients = %s, difficulty = %s WHERE id = %s"
        cursor.execute(sql, (ingredients_str, difficulty, recipe_id))
    else:
        print("Invalid choice.")
        return
    
    conn.commit()
    print("Recipe updated successfully.")

def delete_recipe(conn, cursor):
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()
    
    if not recipes:
        print("No recipes available to delete.")
        return
    
    print("Recipes:")
    for r in recipes:
        print(f"{r[0]}. {r[1]}")
        
    recipe_id = int(input("Enter the ID of the recipe to delete: "))
    
    # Check if recipe exists
    cursor.execute("SELECT id FROM Recipes WHERE id = %s", (recipe_id,))
    if cursor.fetchone() is None:
        print("Recipe with that ID does not exist.")
        return
    
    cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
    conn.commit()
    print("Recipe deleted successfully.")

def main_menu(conn, cursor):
    while True:
        print("\nRecipe Manager Menu")
        print("1. Create a Recipe")
        print("2. Search for a Recipe by Ingredient")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            print("Exiting... Saving changes.")
            conn.commit()
            cursor.close()
            conn.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    conn, cursor = connect_database()
    main_menu(conn, cursor)
