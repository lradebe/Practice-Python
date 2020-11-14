def simple_calculator(a, b, operator):

    """This is a very basic calculator that only works with two
    numbers"""
    
    print(a, operator, b)

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

    print("\nThank you for using this calculator.")

simple_calculator(2,2, "-")
