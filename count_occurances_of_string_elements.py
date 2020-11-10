def count_occurances_of_list_element(List,element):

    count = 0

    for i in List:
        if i == element:
            count += 1
    print(count)

List, element = [1, 2, 3, 4, 5, 5], 5
count_occurances_of_list_element(List, element)
