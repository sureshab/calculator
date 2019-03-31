import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):

    def test_add_method_invalid_inputs(self):
        self.assertRaises(ValueError, Calculator.add, '7', '1')

    def test_add_method_success(self):
        result = Calculator.add(7, 9)
        self.assertEqual(result, 16)

    def test_subtract_invalid_inputs(self):
        self.assertRaises(ValueError, Calculator.add, '7', 1)

    def test_subtract_success(self):
        result = Calculator.subtract(7.5, 2.5)
        self.assertEqual(result, 5.0)

    def test_multiply_invalid_inputs(self):
        self.assertRaises(ValueError, Calculator.multiply, None, None)

    def test_multiply_success(self):
        result = Calculator.multiply(4, 2.0)
        self.assertEqual(result, 8.0)

    def test_div_invalid_types(self):
        self.assertRaises(ValueError, Calculator.div, 'one', 2)

    def test_div_zero_division_error(self):
        self.assertRaises(ZeroDivisionError, Calculator.div, 7, 0)

    def test_div_success(self):
        result = Calculator.div(4,2)
        self.assertEqual(result, 2)
