import unittest

from calculator import (calculate,
                        CalculatorException, InvalidOperationException)


class CalculatorTestCase(unittest.TestCase):
    def test_calculator_adds_two_numbers(self):
        result = calculate(2, 3, 'add')
        self.assertEqual(result, 5)

    def test_calculator_adds_negative_numbers(self):
        result = calculate(2, -3, 'add')
        self.assertEqual(result, -1)

    def test_calculator_multiplies_two_numbers(self):
        result = calculate(4, 3, 'multiply')
        self.assertEqual(result, 12)

    def test_calculator_multiplies_negative_numbers(self):
        result = calculate(3, -1, 'multiply')
        self.assertEqual(result, -3)

    def test_calculator_raises_with_wrong_argument(self):
        with self.assertRaises(CalculatorException):
            calculate(3, "invalid", 'add')

    def test_calculator_raises_with_wrong_operation(self):
        with self.assertRaises(InvalidOperationException):
            calculate(3, 2, 'invalid')
