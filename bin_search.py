import random
import math

def bin_search(arr, num):
	"""
	function get searching value
	and return index of finding element
	and count of cycles
	"""
	index = math.ceil(len(arr) / 2)
	delta = math.ceil(index / 2)
	cnt = 1
	while 1<2:
		if arr[index] > num:
			index -= delta
		elif arr[index] < num:
			index += delta
		else:
			return (index, cnt)
		delta = math.ceil(delta / 2)
		cnt += 1


arr = [random.randint(1,1000) for i in range(1000)]
arr = list(set(arr))
arr.sort()

print(arr)

searching_number = int(input())

print(bin_search(arr, searching_number))