def simple_calculator(a, b, operator):

    """This is a very basic calculator that only works with two
    numbers"""

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

    print("Thank you for using this calculator.")

simple_calculator(2,2, "-")
