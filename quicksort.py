from typing import Any, List


def quickSort(arr: List[Any]) -> List:
    if len(arr) < 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [i for i in arr if i < pivot]
    midle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]
    return quickSort(left) + midle + quickSort(right)


print(quickSort([4, 7, 1, 3, -2, 5, 10, 6]))
