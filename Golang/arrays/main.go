package main

import "fmt"

func main() {
	var ages [5]int = [5]int{29, 30, 31, 32, 33}
	fmt.Println(ages)
	fmt.Println(ages[0])

	// Array of strings
	var names [3]string = [3]string{"Walter", "Taya", "Mariana"}
	fmt.Println(names)

	var ages2 = [5]int{29, 30, 31, 32, 33}
	fmt.Println(ages2)

	ages3 := [5]int{29, 30, 31, 32, 33}
	fmt.Println(ages3)

	// Slices - similar to arrays but more flexible, can grow or shrink
	var scores = []int{29, 30, 31, 32, 33}
	scores[2] = 35
	scores = append(scores, 36)
	fmt.Println(scores, len(scores))

	// Slice ranges

	// [start:stop] - start is included, stop is excluded
	// [start:] - start is included, stop is end of slice
	// [:stop] - start is beginning of slice, stop is excluded
	// [:] - start is beginning of slice, stop is end of slice
	fmt.Println(scores[1:3])
	fmt.Println(scores[:3])
	fmt.Println(scores[1:])
	fmt.Println(scores[:])
}
