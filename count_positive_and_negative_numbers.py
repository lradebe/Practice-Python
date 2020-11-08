def count_positive_and_negative_numbers(List):

    negative_count = 0
    positive_count = 0

    for number in List:
        if number < 0:
            negative_count += 1
        else:
            positive_count += 1


    print("Negative count:",negative_count)
    print("Positive count:",positive_count)


if __name__ == "__main__":

    List = [75,-20,17,-2]
    count_positive_and_negative_numbers(List)
