import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,           # When functions are stored only and not used, remove "()"
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

def calculator():
    first_number = float(input("What's the first number? "))

    continue_calculating = True
    while continue_calculating:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        next_number = float(input("What's the next number? "))
        result = operations[operation_symbol](first_number, next_number)

        print(f"{first_number} {operation_symbol} {next_number} = {result}")
        next_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if next_calculation == 'n':
            continue_calculating = False
            print("\n" * 20)
            print(art.logo)
            calculator()

        else:
            first_number = result

calculator()
