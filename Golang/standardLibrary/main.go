package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	openingQuote := "The first step is to establish that something is possible; then probability will occur."
	fmt.Println(openingQuote)
	fmt.Println(strings.ToUpper(openingQuote))
	fmt.Println(strings.ToLower(openingQuote))
	// fmt.Println(strings.Title(openingQuote)) // Deprecated
	fmt.Println(strings.Replace(openingQuote, "is", "was", -1))
	fmt.Println(strings.Contains(openingQuote, "step"))
	fmt.Println(strings.Index(openingQuote, "step"))
	fmt.Println(strings.Count(openingQuote, "step"))
	fmt.Println(strings.Split(openingQuote, ";"))
	fmt.Println(strings.Fields(openingQuote))

	ages := []int{99, 45, 23, 67, 12, 34, 56, 78, 90}
	sort.Ints(ages)
	fmt.Println(ages)

	index := sort.SearchInts(ages, 67)
	fmt.Println(index)

	names := []string{"Walter", "Taya", "Miguel", "Luis", "Carlos", "Ana", "Maria", "Jose", "Pedro"}
	sort.Strings(names)
	fmt.Println(names)

	fmt.Println(sort.SearchStrings(names, "Miguel"))
}
