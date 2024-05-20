package main

import "fmt"

func main() {
	x := 0
	for x < 4 {
		fmt.Println(x)
		x++
	}

	for i := 0; i < 4; i++ {
		fmt.Println("The value of i is", i)
	}

	names := []string{"Walter", "Taya", "Miguel", "Luis", "Carlos", "Ana", "Maria", "Jose", "Pedro"}
	for i := 0; i < len(names); i++ {
		fmt.Println(names[i])
	}

	for i, name := range names {
		fmt.Println(i, name)
	}

	// _ is used to ignore the index
	for _, name := range names {
		fmt.Println(name)
	}
}
