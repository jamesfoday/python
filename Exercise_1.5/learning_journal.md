# Learning Journal - Exercise 1.5 Task: Recipe App Using OOP

## Overview

In this task, I applied Object-Oriented Programming (OOP) principles to create a Python Recipe application. Instead of using dictionaries to represent recipes, I built a `Recipe` class with data attributes and custom methods, making the code cleaner, more modular, and reusable.

---

## What I Did

- **Class Definition:**  
  Created a `Recipe` class with attributes: `name`, `ingredients`, `cooking_time`, and `difficulty`. I used a class variable `all_ingredients` to track all unique ingredients across recipes.

- **Methods:**  
  Implemented initialization (`__init__`), getters and setters, and various procedural methods like:
  - `add_ingredients()` to add multiple ingredients dynamically
  - `calculate_difficulty()` to assign difficulty level based on cooking time and number of ingredients
  - `search_ingredient()` to check if a recipe contains a specific ingredient
  - `update_all_ingredients()` to update the class-level ingredients list
  - A string representation method (`__str__`) for neat recipe output
  - A static method `recipe_search()` to find recipes containing a given ingredient from a list of Recipe objects

- **Testing:**  
  Created several `Recipe` objects such as Tea, Coffee, Cake, and Banana Smoothie with different ingredients and cooking times. Printed their details and tested the search functionality for ingredients like "Water", "Sugar", and "Bananas".

---

## What I Learned

- How to structure classes and use class variables effectively for shared data (`all_ingredients`).
- How to implement custom methods to encapsulate functionality related to each object.
- The importance of clean string representations for easy debugging and display.
- Using static methods for operations related to a class but not tied to any single object.
- The power of OOP to make programs more maintainable and scalable compared to using plain dictionaries.
- How to manage and search through complex data stored as objects rather than raw data structures.

---

## Challenges

- Designing the logic to keep `all_ingredients` updated correctly as ingredients are added dynamically.
- Managing the interaction between instance-level attributes and class-level variables.
- Ensuring difficulty was calculated and updated only when necessary.

---

## Next Steps

- Extend this application with file handling to save and load recipes from disk.
- Explore inheritance by creating subclasses like `BakingRecipe` or `BeverageRecipe`.
- Add more user interaction, like editing or deleting recipes through methods.

---

## Conclusion

This task solidified my understanding of OOP fundamentals in Python, especially how classes help model real-world entities and behaviors cleanly. It was rewarding to see how encapsulation and method design improve the quality and readability of the code compared to procedural approaches.
