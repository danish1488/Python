import os

# Function to greet the user
def greetMe():
    return "Hello from Python"

# Function to add two numbers
def addition(number1, number2):
    return number1 + number2

# Function to increase a number by 10
def increaseByTen(number):
    return number + 10

# Function to take multiple values and sum them
def takeMultipleValues(*numbers):
    sumOf = sum(numbers)
    return sumOf

# Function to clear the screen
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to get user information and return it as a list
def getUserInformation(firstname, lastname, age):
    return [firstname, lastname, age]
