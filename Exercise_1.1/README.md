# Exercise 1.1 - Python Basics and Environment Setup

## Overview

In this exercise, I set up my Python development environment and completed the following tasks:

- Installed Python (version 3.8.7 recommended) and set up a virtual environment named `cf-python-base`.
- Installed IPython in the virtual environment for an enhanced interactive shell experience.
- Created a Python script `add.py` that:
  - Takes two numbers as input from the user.
  - Adds the numbers together.
  - Prints the result.
- Created a `requirements.txt` file that lists the installed packages in the virtual environment.
- Created a new folder named `Exercise_1.1` to organize all deliverables.
- Moved the script and requirements file into the `Exercise_1.1` folder.
- Committed and pushed the changes to GitHub.

## How to Run

1. Activate your virtual environment:

   ```bash
   workon cf-python-base

2. Navigate to the Exercise_1.1 folder:
cd Exercise_1.1

3.Run the Python script:
python add.py

4. Follow the prompts to enter two numbers, and the program will output their sum.

# How to Set Up the Environment on Another Machine

1.Clone this repository.

2.Create and activate a new virtual environment:
mkvirtualenv cf-python-copy
workon cf-python-copy

Install the required packages from the requirements.txt file:
pip install -r Exercise_1.1/requirements.txt

# Notes
-IPython was installed for better interactive development.
-Virtual environments help manage dependencies and prevent conflicts between projects.

End of Exercise 1.1 README
---