import random


def bin_search(arr, num):
    """
    function get searching value
    and return index of finding element
    """
    index = int(len(arr) / 2)
    delta = int(index / 2)

    while True:
        if arr[index] > num:
            index -= delta
        elif arr[index] < num:
            index += delta
        else:
            return index
        delta = int(delta / 2)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = 8
index = bin_search(array, number)

print(f'Initial array: {array}')
print(f'Initial number: {number}')
print(f'Index of this number is: {index}')

