def simple_calculator():

    """This is a very basic calculator that only works with two numbers"""

    a = input("What is the first digit? ")
    a = int(a)
    operator = input("\nSum(+), subtract(-), multiplication(*), Root(**), Divide(// or /)? ")
    b = input("\nWhat is the second digit? ")
    b = int(b)

    print("\n\tQuestion: ", a, operator, b)

    if operator == "+":
        c = a + b
        print("Answer:",c)

    elif operator == "-":
        c = a - b
        print("Answer:",c)

    elif operator == "/":
        c = a / b
        print("Answer:",c)

    elif operator == "//":
        c = a // b
        print("Answer:",c)

    elif operator == "*":
        c = a * b
        print("Answer:",c)

    elif operator == "**":
        c = a ** b
        print("Answer:",c)

def function_info(function_name):
    """This function should return information about any function that has a docstring"""


    print(function_name.__doc__)

function_info(simple_calculator)
