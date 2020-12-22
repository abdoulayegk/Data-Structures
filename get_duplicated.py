def get_duplicated(arr):
    result = set()
    i = 0
    while i < len(arr):
        if arr[i] in result:
            arr.pop()
        else:
            result.add(arr[i])
            i += 1


if __name__ == '__main__':
    arr_list = [2, 4, 3, 4, 2, 1, 5]
    get_duplicated(arr_list)
    print(arr_list)
