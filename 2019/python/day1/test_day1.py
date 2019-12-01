import unittest
from day1 eimport calculate_fuel_required


class TestAdventDayOne(unittest.TestCase):
    def test_day_one(self):
        received = calculate_fuel_required(12)
        expected = 2
        self.assertTrue(received, expected)

        received = calculate_fuel_required(14)
        expected = 2
        self.assertTrue(received, expected)

        received = calculate_fuel_required(1969)
        expected = 654
        self.assertTrue(received, expected)

        received = calculate_fuel_required(100756)
        expected = 33583
        self.assertTrue(received, expected)
