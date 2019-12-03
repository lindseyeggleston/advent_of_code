import unittest

from day2 import intcode_decoder


class TestIntcodeProgram(unittest.TestCase):
    def test_intcode_decoder(self):
        got = intcode_decoder([1, 0, 0, 0, 99])
        expected = [2, 0, 0, 0, 99]
        self.assertTrue(got, expected)

        got = intcode_decoder([2, 3, 0, 3, 99])
        expected = [2, 3, 0, 6, 99]
        self.assertTrue(got, expected)

        got = intcode_decoder([2, 4, 4, 5, 99, 0])
        expected = [2, 4, 4, 5, 99, 9801]
        self.assertTrue(got, expected)

        got = intcode_decoder([1, 1, 1, 4, 99, 5, 6, 0, 99])
        expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        self.assertTrue(got, expected)