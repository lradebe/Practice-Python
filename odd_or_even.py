def odd_or_even(number):
    """This function takes a number and reveals whether it is an even 
    number or odd"""

    number = int(number)
    if number % 2 == 0:
        print("This is an even number:",number)


    else:
        print("This is an odd number:",number)

odd_or_even("9")

def odd_or_even_in_List(List):
    """This function takes a list and reveals which numbers are odd
    and which are even"""

    Even = []
    Odd = []

    for item in List:
        if item % 2 == 0:
            even = item
            Even.append(even)
        else:
            odd = item
            Odd.append(odd)

    print("This is the even list:",Even)
    print("This is the odd list:",Odd)

odd_or_even_in_List([1,2,3,4,5,6,7,8,9,10])

def odd_or_even_counter_in_List(List):
    """This function counts the occurance of even and odd numbers"""

    even_count = 0
    odd_count = 0
    for item in List:
        if item % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("Here is the number of even numbers in the List:",even_count)
    print("Here is the number of odd numbers in the List:",odd_count)

odd_or_even_counter_in_List([1,2,3,4,5,6,7,8,9,10])
