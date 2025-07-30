# Learning Journal: Exercise 1.3 - Recipe Input and Data Handling

## What did I learn?

In this exercise, I learned how to collect user input for recipes using Python, including recipe name, cooking time, and ingredients. I practiced storing this data in appropriate Python data structures like lists and dictionaries. I also explored methods for processing and cleaning input data, such as removing duplicate ingredients and sorting them.

I understood the importance of handling user input carefully to avoid errors, especially when converting string inputs to numbers. Additionally, I practiced using list comprehensions and basic built-in methods like `split()`, `join()`, and `sorted()`.

## Challenges faced

One challenge I encountered was handling invalid user inputs, such as non-numeric strings when expecting numbers for cooking time or ingredient counts. Initially, my program would crash when such inputs were provided. I recognized the need for exception handling to make the program more robust and user-friendly.

Another challenge was efficiently removing duplicate ingredients while preserving their order. I learned that there are multiple ways to achieve this, including using `list(set(...))`, `dict.fromkeys()`, or checking existence before adding to a list.

## How did I apply the tutor’s recommendations?

- **Exception handling:** I added `try-except` blocks to catch `ValueError` exceptions when converting input strings to integers. This prevents the program from crashing and allows me to notify users of invalid inputs.

- **Memory optimization:** I avoided unnecessary variable assignments when they are not needed elsewhere in the code, reducing memory usage.

- **Duplicate removal:** Besides using the method taught in the exercise, I learned alternative Pythonic ways like `list(set(ingredients_list))` and `list(dict.fromkeys(ingredients_list))`. These alternatives are helpful depending on whether order matters.

- **Sorting:** I replaced in-place sorting (`list.sort()`) with `sorted(list)` to preserve the original list, which is a better practice to avoid unintended side effects.

- **Use of underscore `_`:** I continued using `_` for ignored variables when unpacking, which improves code readability by indicating that the variable is not used.

## What would I do differently next time?

Next time, I would focus earlier on implementing comprehensive input validation and exception handling to improve user experience. I would also modularize the code further, breaking down input and processing logic into smaller functions for better readability and testability.

Additionally, I would experiment more with Python’s data structures and built-in functions to optimize the code for both clarity and performance.

## Summary

Exercise 1.3 helped me deepen my understanding of collecting and handling user input in Python, as well as managing data structures efficiently. The tutor’s feedback provided valuable insights into writing more robust and optimized code, which I have incorporated and will continue to apply in future exercises.
