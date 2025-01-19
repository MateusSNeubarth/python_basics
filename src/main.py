import os
from simple_calculator import calculator

print("Welcome to Python Basics, some basic examples of Python Algorithms!")

while True:
    os.system("cls")
    print("1 - Simple Calculator")
    print("2 - Password Generator")
    print("3 - Unity Conversor")
    print("4 - Guessing Game")
    print("5 - Timer")
    print("X - Exit")
    input = input("Please, select the algorithm you'd like to see")

    match input:
        case "1":
            os.system("cls")
            calculator()
        case "2":
            os.system("cls")
            print("TO DO - Password Generator")
        case "3":
            os.system("cls")
            print("TO DO - Unity Conversor")
        case "4":
            os.system("cls")
            print("TO DO - Guessing Game")
        case "5":
            os.system("cls")
            print("TO DO - Timer")
        case "X":
            break


print("Thanks for utlizing my app!")
