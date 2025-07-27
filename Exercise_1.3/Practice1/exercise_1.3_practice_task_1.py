

# Step 1: Get input values from the user
first_term = int(input("Enter the first term: "))
second_term = int(input("Enter the second term: "))
operation = input("Enter the operation (+ or -): ")

# Step 2: Use if-elif-else to decide the operation
if operation == '+':
    result = first_term + second_term
    print(f"The result of addition is: {result}")
elif operation == '-':
    result = first_term - second_term
    print(f"The result of subtraction is: {result}")
else:
    print("Unknown operator. Please enter either + or -.")
