# Function to convert a number in word form to its corresponding integer
def word_to_number(word):
    words_to_numbers = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10
    }
    return words_to_numbers.get(word.lower())

# Function to get a valid number from the user (either word or digit)
def get_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():  # Directly convert if it's a digit
            return int(user_input)
        elif user_input.isalpha():  # Check for word-form number
            number = word_to_number(user_input)
            if number is not None:
                return number
        print("Invalid input. Please enter a valid number (e.g., '2' or 'two').")

# Get the first number from the user
first_number = get_number("Enter your first number (digit or word): ")

# Get the second number from the user
second_number = get_number("Enter your second number (digit or word): ")

# Ask the user which operation they want to perform
operation = input("Choose an operation (+, -, *, /): ")

# Perform the operation and display the result
if operation == "+":
    print(f"The result of {first_number} + {second_number} is {first_number + second_number}.")
elif operation == "-":
    print(f"The result of {first_number} - {second_number} is {first_number - second_number}.")
elif operation == "*":
    print(f"The result of {first_number} * {second_number} is {first_number * second_number}.")
elif operation == "/":
    if second_number != 0:
        print(f"The result of {first_number} / {second_number} is {first_number / second_number:.2f}.")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose +, -, *, or /.") 
