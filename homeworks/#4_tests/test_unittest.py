import unittest
from functions_to_test import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(5, 4), 9)
        self.assertEqual(Calculator.add(0.78, 1.52), 2.3)
        self.assertRaises(TypeError, Calculator.add, '1', 2)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(3, 7), -4)
        self.assertEqual(Calculator.subtract(6.4, 2), 4.4)
        self.assertRaises(TypeError, Calculator.subtract, '1', 2)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(10, 2), 20)
        self.assertEqual(Calculator.multiply(80, 0.5), 40)
        self.assertEqual(Calculator.multiply('1', 2), '11')
        self.assertRaises(TypeError, Calculator.multiply, None, 2)

    def test_divide(self):
        self.assertRaises(ValueError, Calculator.divide, 8, 0)
        self.assertEqual(Calculator.divide(20, 4), 5)
        self.assertEqual(Calculator.divide(3, 4), 0.75)
        self.assertRaises(TypeError, Calculator.divide, '1', 2)


if __name__ == '__main__':
    unittest.main()
