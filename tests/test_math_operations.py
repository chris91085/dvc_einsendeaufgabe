# tests/test_math_operations.py
import unittest
from calculator.math_operations import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(3, 5), 8)
        self.assertEqual(Calculator.add(-1, 1), 0)
    
    def test_subtract(self):
        self.assertEqual(Calculator.subtract(10, 4), 6)
        self.assertEqual(Calculator.subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(Calculator.multiply(3, 5), 15)
        self.assertEqual(Calculator.multiply(-2, 3), -6)
    
    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 2), 5)
        self.assertEqual(Calculator.divide(-6, 3), -2)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
