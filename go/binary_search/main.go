package main

import (
	"fmt"
	"math"
)

func bin_search(arr []int, element int) int {
	index := (len(arr)) / 2
	step := index
	for arr[index] != element {
		step = int(math.Round(float64(step) / 2))
		if arr[index] < element {
			index += step
		} else {
			index -= step
		}
	}
	return index
}

func test(value1 int, value2 int) {
	if value1 == value2 {
		fmt.Printf("Test passed, %v equal %v\n", value1, value2)
	} else {
		fmt.Printf("Test failed, %v not equal %v\n", value1, value2)
	}
}

func main() {
	arr := []int{1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23}

	test(bin_search(arr, 1), 0)
	test(bin_search(arr, 3), 1)
	test(bin_search(arr, 5), 2)
	test(bin_search(arr, 7), 3)
	test(bin_search(arr, 9), 4)
	test(bin_search(arr, 11), 5)
	test(bin_search(arr, 13), 6)
	test(bin_search(arr, 15), 7)
	test(bin_search(arr, 17), 8)
	test(bin_search(arr, 19), 9)
	test(bin_search(arr, 21), 10)
	test(bin_search(arr, 23), 11)
}
