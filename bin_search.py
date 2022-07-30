class NotFound(Exception):
    pass


def bin_search(arr: list[int], num: int) -> int:
    """
    function get searching value
    and return index of finding element
    """
    low: int = 0
    high: int = len(arr) - 1

    while low <= high:
        mid: int = int((low + high) / 2)
        guess: int = arr[mid]
        if guess == num:
            return mid
        if guess > num:
            high = mid - 1
        else:
            low = mid + 1

    raise NotFound


array: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number: int = 1
position: int = bin_search(array, number)

print(f'Initial array: {array}')
print(f'Initial number: {number}')
print(f'Position of this number is: {position}')
