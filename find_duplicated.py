"""To find all duplicate elements in an array in O(n) time and O(1) space """


def find_duplicates(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i])] > 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print('Duplicate', abs(arr[i]))


assert find_duplicates([6, 1, 3, 3, 3, 6, 6]) == 6, 3
