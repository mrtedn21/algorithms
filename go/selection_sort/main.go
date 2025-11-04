package main

import (
	"fmt"
	"slices"
)

func FindMin(arr []int) (int, int) {
	min := arr[0]
	min_index := 0
	for index, num := range arr {
		if num < min {
			min = num
			min_index = index
		}
	}
	return min_index, min
}

func SelectionSort(arr []int) []int {
	res := []int{}
	len_arr := len(arr)

	for range len_arr {
		min_index, min_value := FindMin(arr)
		res = append(res, min_value)
		arr = slices.Delete(arr, min_index, min_index+1)
	}
	return res
}

func main() {
	arr := []int{234, 123, 111, 222, 444, 555}
	fmt.Println("Initial array")
	fmt.Println(arr)

	sorted_arr := SelectionSort(arr)
	fmt.Println("Sorted array")
	fmt.Println(sorted_arr)
}
