package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func raiseError(err error) {
	if err != nil {
		panic(err)
	}
}

func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func CalculateFuel(weight int) int {
	return Max(weight/3-2, 0)
}

func CalculateModuleFuelRequirements(weightFile string) int {
	openFile, err := os.Open(weightFile)
	raiseError(err)

	scanner := bufio.NewScanner(openFile)
	scanner.Split(bufio.ScanLines)
	var totalFuel int
	for scanner.Scan() {
		weight, err := strconv.ParseInt(scanner.Text(), 10, 64)
		raiseError(err)
		totalFuel += CalculateFuel(int(weight))
	}
	return totalFuel
}

func CalculateTotalFuelRequirements(weightFile string) int {
	openFile, err := os.Open(weightFile)
	raiseError(err)

	scanner := bufio.NewScanner(openFile)
	scanner.Split(bufio.ScanLines)
	var totalFuel int
	return totalFuel
}

func main() {
	fmt.Println(CalculateModuleFuelRequirements("../../data/day1.txt"))
}
