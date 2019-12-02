package main

import "testing"

const testFilePath = "../../data/day1_test.txt"

func TestFuel(t *testing.T) {
	assertCorrectNumber := func(t *testing.T, got, want int) {
		t.Helper()
		if got != want {
			t.Errorf("got %d, expected %d", got, want)
		}
	}

	t.Run("calculate fuel for mass of 12", func(t *testing.T) {
		got := CalculateFuel(12)
		want := 2
		assertCorrectNumber(t, got, want)
	})

	t.Run("calculate fuel for mass of 14", func(t *testing.T) {
		got := CalculateFuel(14)
		want := 2
		assertCorrectNumber(t, got, want)
	})

	t.Run("calculate fuel for mass of 1969", func(t *testing.T) {
		got := CalculateFuel(1969)
		want := 654
		assertCorrectNumber(t, got, want)
	})

	t.Run("calculate fuel for mass of 100756", func(t *testing.T) {
		got := CalculateFuel(100756)
		want := 33583
		assertCorrectNumber(t, got, want)
	})

	t.Run("calculate total fuel for models in test.txt", func(t *testing.T) {
		got := CalculateModuleFuelRequirements(testFilePath)
		want := 34241
		assertCorrectNumber(t, got, want)
	})

	t.Run("calculate total fuel for modules and fuel in test.txt", func(t *testing.T) {
		got := CalculateTotalFuelRequirements(testFilePath)
		want := 51316
		assertCorrectNumber(t, got, want)
	})

}
