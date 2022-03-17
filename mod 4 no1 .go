package main

import "fmt"

//Maria Christine 1303210041
func main() {
	var n, a, r, hasil, i int
	fmt.Scanln(&n, &a, &r)
	fmt.Print("0")
	i = 1
	for i <= n {
		hasil = i * a * r
		fmt.Print(" + ", hasil)
		i = i + 1
	}
}
