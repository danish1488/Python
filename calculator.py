# Get the first number from the user
first_number = int(input("Enter your first number: "))

# Get the second number from the user
second_number = int(input("Enter your second number: "))

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