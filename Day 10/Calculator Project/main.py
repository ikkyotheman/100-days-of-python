# TODO: Write out the other 3 functions - subtract, multiply and divide.
import art
print(art.logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# my_favourite_calculation = input('Enter your favourite calculation: ')

# TODO: TODO: Add these 4 functions into a dictionary
#  as the values. Keys = "+", "-", "*", "/"

operations = {
   "+": add,
   "-": subtract,
   "*": multiply,
   "/": divide,
}

# TODO: Use the dictionary operations to perform the calculations.
#  Multiply 4 * 8 using the dictionary.
def calculator():
    number_1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    refactor = True
    while refactor:
        operator = input("Pick an operation: ")
        number_2 = float(input("What's the next number? "))
        solution = operations[operator](number_1, number_2)
        print(f"{number_1} {operator} {number_2} = {solution}")
        response = input(f"Type 'y' to continue calculating with {solution}, or type 'n' to start a new calculation: ")
        if response == "y":
            start_new = False
            refactor = True
            number_1 = solution
        elif response == "n":
            refactor = False
            print("\n" * 20)
            calculator()
calculator()