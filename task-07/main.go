package main

import (
	"fmt"
	"math/big"
)

var Count = 0

func main() {
	var num big.Int
	num.SetInt64(0)

	for {
		fmt.Println("Correct number", num.String())
		fmt.Println("Enter 1 to increment the number, or 2 to decrement the number")

		var input int
		fmt.Scan(&input)

		if input == 1 {
			num.Add(&num, big.NewInt(1))
		} else if input == 2 {
			num.Sub(&num, big.NewInt(1))
		} else if input == 0 {
			num.Sub(&num, num.SetInt64(0))
		}
	}
}
