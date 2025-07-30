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

## Reflection and Learnings

- I learned the importance of keeping class variables like `all_ingredients` synchronized with instance data, which was challenging but reinforced understanding of class vs instance scope.
- Implementing getters and setters made me appreciate encapsulation and how controlled access to attributes can improve code maintainability.
- Calculating difficulty dynamically only when related attributes change was a key insight—this mirrors real-world programming concerns about performance and data integrity.
- Using static methods for tasks like searching across objects helped me understand how OOP can logically group related functionality, even when it doesn't act on a single instance.
- The separation of responsibilities in methods improved readability and made the code easier to debug and extend.
- I realized the benefit of overriding `__str__` and `__repr__` methods to provide useful object representations for debugging and user interaction.

---

## Challenges

- Handling updates to both instance and class variables in a consistent and error-free manner required careful thought and testing.
- Ensuring the difficulty recalculates correctly whenever cooking time or ingredients change was initially tricky because changes in ingredients didn’t always trigger recalculation.
- Balancing the use of class variables and instance variables without causing unexpected side effects was a complex design consideration.

---

## What I Would Do Differently Next Time

- Use Python’s `@property` decorator to better manage getters and setters, making the API more Pythonic and reducing boilerplate.
- Use a `set` data structure for ingredients instead of a list to automatically handle uniqueness and improve membership checks.
- Add methods specifically for updating cooking time and ingredients that internally handle difficulty recalculation, avoiding the need for external ordering of method calls.
- Write unit tests to ensure that changes in data correctly propagate to dependent attributes like difficulty.

---

## Next Steps

- Extend this class to support saving and loading from files or databases.
- Explore Python’s dataclasses module to reduce boilerplate code for data containers like Recipe.
- Implement more advanced search and filtering methods for collections of recipes.
- Practice writing property decorators and better encapsulation techniques.

---

## Conclusion

This exercise was instrumental in deepening my understanding of OOP concepts in Python. It showed me the value of well-structured classes, the power of encapsulation, and how static methods can organize functionality cleanly. The reflections and challenges highlighted areas for improvement that I plan to address in future coding tasks.

