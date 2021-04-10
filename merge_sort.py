def merge_sort(list):
    """sorts a list in ascending order
    return a new sorted list
    Divide: find the mid value of the linst and divide it into sublists
    Conquer: Recursively sort the sublist created in the privious step
    Combine: merge the sorted sublists create in the privous step"""
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)


def split(list):
    """Implementation of the split funciton"""
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    return left, right


def merge(left, right):
    """Merge the two created list"""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


alist = [23, 5, 123, 55, 32, 2, 9, 20, 1, 43]
test = merge_sort(alist)
print(test)
