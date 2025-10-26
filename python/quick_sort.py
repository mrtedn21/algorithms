def easy_sort(arr: list[int]) -> list[int]:
    """ this function get list with only two elements and sort it"""
    if arr[0] < arr[1]:
        return arr
    else:
        temp: int = arr[1]
        arr[1] = arr[0]
        arr[0] = temp
        return arr


def quick_sort(arr: list[int]) -> list[int]:
    """ this function get list of any len and return sorted list"""
    if len(arr) == 2:
        return easy_sort(arr)
    if len(arr) < 2:
        return arr

    initial_element: int = arr[0]
    left_arr: list[int] = []
    right_arr: list[int] = []

    for element in arr[1:]:
        if element < initial_element:
            left_arr.append(element)
        else:
            right_arr.append(element)

    return quick_sort(left_arr) + [initial_element] + quick_sort(right_arr)


initial_arr: list[int] = [4, 5, 1, 7, 5, 2, 6, 7, 4, 3, 6, 4, 3, 1, 4, 5, 6]
sorted_arr: list[int] = quick_sort(initial_arr)

print(f'Initial arr: {initial_arr}')
print(f'Sorted arr: {sorted_arr}')
