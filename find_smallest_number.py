def find_smallest_number(List):
    """Find the smallest number in List"""

    Small = min(List)

    print("Original list:",List)
    print("\n\t\tSmallest number in List:", Small)
    print("Sorted from smallest to biggest:",sorted(List))
    print("Sorted from biggest to smallest:",
    sorted(List, reverse = True))


List = [7, 3, 4, 9, 2, 5, 10, 1, 6, 8]
find_smallest_number(List)


