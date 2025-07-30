from sqlalchemy import create_engine, Column, Integer, String, and_
from sqlalchemy.orm import sessionmaker, declarative_base

# Database connection
engine = create_engine('mysql+mysqlconnector://cf-python:password@localhost/task_database')

# Session setup
Session = sessionmaker(bind=engine)
session = Session()

# Base class for model
Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'final_recipes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe ID: {self.id} - {self.name} ({self.difficulty})>"

    def __str__(self):
        return (
            f"\n{'-'*40}\n"
            f"Recipe ID:\t{self.id}\n"
            f"Name:\t\t{self.name}\n"
            f"Ingredients:\t{self.ingredients}\n"
            f"Cooking Time:\t{self.cooking_time} minutes\n"
            f"Difficulty:\t{self.difficulty}\n"
            f"{'-'*40}\n"
        )

    def calculate_difficulty(self):
        count = len(self.return_ingredients_as_list())
        if self.cooking_time < 10 and count < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and count >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and count < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        return [i.strip() for i in self.ingredients.split(",")]

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

def create_recipe():
    name = input("Enter recipe name (max 50 chars): ").strip()
    if len(name) == 0 or len(name) > 50:
        print("Invalid name length!")
        return
    
    try:
        cooking_time = int(input("Enter cooking time (minutes): ").strip())
    except ValueError:
        print("Invalid cooking time! Must be a number.")
        return

    try:
        num_ingredients = int(input("How many ingredients? ").strip())
        if num_ingredients <= 0:
            print("Number of ingredients must be positive.")
            return
        ingredients = []
        for i in range(num_ingredients):
            ing = input(f"Ingredient {i + 1}: ").strip()
            if not ing:
                print("Ingredient cannot be empty.")
                return
            ingredients.append(ing)
        ingredients_str = ", ".join(ingredients)
    except ValueError:
        print("Invalid number of ingredients.")
        return

    recipe_entry = Recipe(
        name=name,
        ingredients=ingredients_str,
        cooking_time=cooking_time
    )
    recipe_entry.calculate_difficulty()
    session.add(recipe_entry)
    session.commit()
    print(f"Recipe '{name}' added successfully!")

def view_all_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found in database.")
        return
    
    for recipe in recipes:
        print(recipe)

def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("No recipes in database.")
        return

    results = session.query(Recipe.ingredients).all()
    all_ingredients = []

    for row in results:
        for ing in row[0].split(","):
            ing = ing.strip()
            if ing not in all_ingredients:
                all_ingredients.append(ing)
    
    all_ingredients.sort()
    print("Available ingredients:")
    for idx, ing in enumerate(all_ingredients, 1):
        print(f"{idx}. {ing}")

    selections = input("Select ingredient numbers separated by spaces: ").strip().split()

    try:
        selections = [int(s) for s in selections]
    except ValueError:
        print("Invalid input, must be numbers.")
        return
    
    if any(s < 1 or s > len(all_ingredients) for s in selections):
        print("Selection out of range.")
        return
    
    search_ingredients = [all_ingredients[s-1] for s in selections]

    conditions = [Recipe.ingredients.like(f"%{ing}%") for ing in search_ingredients]

    filtered_recipes = session.query(Recipe).filter(and_(*conditions)).all()

    if not filtered_recipes:
        print("No recipes found with these ingredients.")
        return
    
    for recipe in filtered_recipes:
        print(recipe)

def edit_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes available to edit.")
        return
    
    results = session.query(Recipe.id, Recipe.name).all()
    print("Recipes:")
    for rid, name in results:
        print(f"{rid}. {name}")

    try:
        recipe_id = int(input("Enter recipe ID to edit: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    
    recipe_to_edit = session.get(Recipe, recipe_id)
    if not recipe_to_edit:
        print("Recipe not found.")
        return

    print(recipe_to_edit)
    print("What do you want to edit?")
    print("1. Name")
    print("2. Cooking Time")
    print("3. Ingredients")

    choice = input("Enter choice (1-3): ").strip()
    
    if choice == "1":
        new_name = input("Enter new name (max 50 chars): ").strip()
        if not new_name or len(new_name) > 50:
            print("Invalid name.")
            return
        recipe_to_edit.name = new_name
    elif choice == "2":
        try:
            new_time = int(input("Enter new cooking time: ").strip())
            recipe_to_edit.cooking_time = new_time
            recipe_to_edit.calculate_difficulty()
        except ValueError:
            print("Invalid cooking time.")
            return
    elif choice == "3":
        new_ingredients = input("Enter new ingredients (comma-separated): ").strip()
        recipe_to_edit.ingredients = new_ingredients
        recipe_to_edit.calculate_difficulty()
    else:
        print("Invalid choice.")
        return

    session.commit()
    print("Recipe updated successfully.")

def delete_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes available to delete.")
        return

    results = session.query(Recipe.id, Recipe.name).all()
    print("Recipes:")
    for rid, name in results:
        print(f"{rid}. {name}")

    try:
        recipe_id = int(input("Enter recipe ID to delete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return

    recipe_to_delete = session.get(Recipe, recipe_id)
    if not recipe_to_delete:
        print("Recipe not found.")
        return
    
    confirm = input(f"Are you sure you want to delete '{recipe_to_delete.name}'? (yes/no): ").strip().lower()
    if confirm == 'yes':
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe deleted.")
    else:
        print("Deletion cancelled.")

def main_menu():
    while True:
        print("\nRecipe Manager Menu")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search recipes by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exit")

        choice = input("Enter your choice: ").strip().lower()
        
        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "quit":
            print("Exiting application...")
            session.close()
            engine.dispose()
            break
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main_menu()
