import unittest, math
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # Set up an instance of the Calculator class for testing
        self.calc = Calculator()

    def test_add(self):
        # Test the add method with positive, negative, and zero values
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        # Test the subtract method with positive, negative, and zero values
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        # Test the multiply method with positive, negative, and zero values
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    def test_divide(self):
        # Test the divide method with positive, negative, and zero values
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(-10, 5), -2)
        self.assertEqual(self.calc.divide(-10, -5), 2)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_square_root(self):
        # Test the square_root method with positive and zero values
        self.assertEqual(self.calc.square_root(16), 4)
        self.assertEqual(self.calc.square_root(0), 0)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

    def test_power(self):
        # Test the power method with positive, negative, and zero values
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(2, -1), 0.5)

    def test_logarithm(self):
        # Test the logarithm method with positive values and different bases
        self.assertAlmostEqual(self.calc.logarithm(math.e), 1)
        self.assertAlmostEqual(self.calc.logarithm(100, 10), 2)
        with self.assertRaises(ValueError):
            self.calc.logarithm(-1)
        with self.assertRaises(ValueError):
            self.calc.logarithm(0)

    def test_factorial(self):
        # Test the factorial method with positive and zero values
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(0), 1)
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)

if __name__ == '__main__':
    unittest.main()