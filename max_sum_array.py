"""
Take an array with positive and negative integers and find the maximum sum of
that array
"""


def max_sum(arr):
    """To find the max sum of of an array"""
    if len(arr) == 0:
        return print("Too small")
    max_sum, current_sum = arr[0], arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum


print(max_sum([3, 4, -2, 12, -6, -9, 10]))
