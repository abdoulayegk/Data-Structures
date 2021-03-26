"""
Given an array what is the most frequently occuring element.
"""


def most_frequent(list_num: list) -> list:
    """docstring for most_frequent
    list: integer
    return a number of most frequent element in the list
    """
    count = {}
    max_count = 0
    max_item = None

    for i in list_num:
        if i not in count:
            count[i] = 1

        else:
            count[i] += 1

        if count[i] > max_count:
            max_count = count[i]
            max_item = i
    print(count)
    return max_item


test_list = [4, 3, 1, 2, 2, 5]
print(most_frequent(test_list))
