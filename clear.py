def clear(List):
    """This function clears contents within a list"""
    print("Original list:",List)
    print("Cleared list:", [List.clear()])

List = [1, 2, 3, "hey", "there", '!']
clear(List)
