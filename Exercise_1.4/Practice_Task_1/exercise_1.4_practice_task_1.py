
numbers = list(range(50, 101))

numbers_str = [str(number) + '\n' for number in numbers]
with open('number_list.txt', 'w') as file:
    file.writelines(numbers_str)
