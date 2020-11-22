def make_list_and_tuple(numbers):
    """This function takes comma-separated numbers and makes a list and tuple of them"""

    print(f"List: {list(numbers)}")
    print(f"Tuple: {tuple(numbers)}")

numbers = 1, 2, 3, 4, 5
make_list_and_tuple(numbers)
