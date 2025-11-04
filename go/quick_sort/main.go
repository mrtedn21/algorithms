package main

import (
	"fmt"
	"slices"
)

func quick_search(arr []int) []int {
	if len(arr) < 2 {
		return arr
	}
	first_element := arr[0]
	less_arr := []int{}
	same_arr := []int{}
	more_arr := []int{}
	for _, element := range arr {
		if element > first_element {
			more_arr = append(more_arr, element)
		} else if element < first_element {
			less_arr = append(less_arr, element)
		} else {
			same_arr = append(same_arr, element)
		}
	}
	return slices.Concat(
		quick_search(less_arr),
		same_arr,
		quick_search(more_arr),
	)
}

func main() {
	l1 := []int{4, 3, 1, 5, 3, 0, 9}
	fmt.Println(quick_search(l1))
}
