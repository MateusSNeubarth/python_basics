"""
SIMPLE CALCULATOR

Just a calculator that is able to make simple operations, such as sum, subtract, multiply and divide
"""


def sum(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def check_numbers():

    valid_numbers = "1234567890"

    while True:
        num1 = input("Enter first number: ")
        if num1 in valid_numbers:
            break
        else:
            print("Not a number")
    while True:
        num2 = input("Enter second number: ")
        if num2 in valid_numbers:
            break
        else:
            print("Not a number")

    return int(num1), int(num2)


def calculator():

    print("------Welcome to Simple Calculator------")
    print("1 - Sum")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    option = input("Select your option: ")

    match option:
        case "1":
            num1, num2 = check_numbers()
            print(f"{num1} + {num2} = {sum(num1, num2)}")
        case "2":
            num1, num2 = check_numbers()
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        case "3":
            num1, num2 = check_numbers()
            print(f"{num1} x {num2} = {multiply(num1, num2)}")
        case "4":
            num1, num2 = check_numbers()
            if num2 == 0:
                print("Can't divide by zero")
            else:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
