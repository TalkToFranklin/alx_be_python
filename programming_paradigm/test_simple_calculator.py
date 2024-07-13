# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertEqual(self.calc.add(-5, -5), -10)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-2, 1), -3)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(4.2, 1.7), 2.5)
        self.assertEqual(self.calc.subtract(-3, -3), 0)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(1.5, 2.0), 3.0)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(-9, -3), 3)
        self.assertEqual(self.calc.divide(5, 0), None)  # Test for division by zero

    def test_edge_cases(self):
        """Test edge cases for each method."""
        self.assertEqual(self.calc.add(1e10, 1e10), 2e10)
        self.assertEqual(self.calc.subtract(1e10, 1e10), 0)
        self.assertEqual(self.calc.multiply(1e10, 1e-10), 1)
        self.assertEqual(self.calc.divide(1e10, 1e10), 1)
        self.assertEqual(self.calc.divide(1, 1e-10), 1e10)

if __name__ == "__main__":
    unittest.main()
