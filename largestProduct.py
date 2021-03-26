"""
Given a list of integers, return the largest product that can be made by
multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since thats
-10 * -10 * 5.

You can assume the list has at least three integers.
"""


def find_product(numbers: list):
    """docstring for find_product"""
    ls = sorted([abs(i) for i in numbers], reverse=True)
    print(ls)
    r = ls[0:3]
    result = 1
    for i in r:
        result *= i
    print(result)


print([-10, -10, -8, 5, 2])
