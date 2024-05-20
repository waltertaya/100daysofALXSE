package main

import "fmt"

func main() {
	//fmt methods
	//Print method
	name := "Walter Taya"
	age := 29
	fmt.Print("Hello, my name is ", name, " and I am ", age, " years old\n")
	//Println method
	fmt.Println("Hello, my name is ", name, " and I am ", age, " years old")
	//Printf method
	fmt.Printf("Hello, my name is %s and I am %d years old\n", name, age)
	// %s : string, %f : float, %d : int, %T : Type
	// %q :
	// %v : general

	// sprintf method - returns a formatted string
	message := fmt.Sprintf("Hello, my name is %s and I am %d years old", name, age)
	fmt.Println(message)
}
