def duplicate_char(input):
    """This function takes characters as input then displays its duplicates
    and doesn't remove the first occurance while it removes the duplicated characters
    into a new variable"""

    input = str(input)
    counter = 0
    duplicate_char = ""
    characters = ""

    for char in input:
        if not char in characters:
            characters += char
        else:
            duplicate_char += char
            counter += 1

    print("Original input:",input)
    print("First occurance Characters:",characters)
    print("Duplicated characters:",duplicate_char)
    print("Number of duplicated characters:",counter)

if __name__ == "__main__":
    input = "Hello_Yellow_Fellow"
    duplicate_char(input)
