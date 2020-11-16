def simple_calculator():

    """This is a very basic calculator that only works with two
    numbers"""
    
    a = input("What is the first digit? ")
    a = int(a)
    operator = input("\nSum(+), subtract(-), multiplication(*), Root(**) ")
    b = input("What is the second digit? ")
    b = int(b)
    
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

simple_calculator()
