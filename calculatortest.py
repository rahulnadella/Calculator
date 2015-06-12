import unittest
import calculator

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = calculator.Calculator()

    def tearDown(self):
        self.calculator = None

    def test_addition_identity(self):
        self.assertEqual(1, self.calculator.add(1, 0))
        self.assertEqual(1, self.calculator.add(0, 1))
        self.assertEqual(-1, self.calculator.add(-1, 0))
        self.assertEqual(-1, self.calculator.add(0, -1))

    def test_addition_of_negatives(self):
        self.assertEqual(1, self.calculator.add(2, -1))
        self.assertEqual(1, self.calculator.add(-1, 2))
        self.assertEqual(-1, self.calculator.add(-2, 1))
        self.assertEqual(-1, self.calculator.add(1, -2))

    def test_subtraction_identity(self):
        self.assertEqual(1, self.calculator.subtract(2, 1))
        self.assertEqual(1, self.calculator.subtract(1, 0))
        self.assertEqual(-1, self.calculator.subtract(0, 1))
        self.assertEqual(-1, self.calculator.subtract(1, 2))

    def test_subtraction_of_negatives(self):
        self.assertEqual(1, self.calculator.subtract(-1, -2))
        self.assertEqual(-1, self.calculator.subtract(-2, -1))
        self.assertEqual(-2, self.calculator.subtract(-1, 1))
        self.assertEqual(3, self.calculator.subtract(1, -2))

    def test_multiplication_identity(self):
        self.assertEqual(0, self.calculator.multiply(4, 0))
        self.assertEqual(6, self.calculator.multiply(3, 2))
        self.assertEqual(6, self.calculator.multiply(2, 3))
        self.assertEqual(0, self.calculator.multiply(0, 4))
        self.assertEqual(0, self.calculator.multiply(2.5, 0))
        self.assertEqual(4.4, self.calculator.multiply(2.2, 2))
        self.assertEqual(4.4, self.calculator.multiply(2, 2.2))

    def test_multiplication_of_negatives(self):
        self.assertEqual(0, self.calculator.multiply(-4, 0))
        self.assertEqual(0, self.calculator.multiply(0, -4))
        self.assertEqual(-6, self.calculator.multiply(-3, 2))
        self.assertEqual(-6, self.calculator.multiply(3, -2))
        self.assertEqual(-6, self.calculator.multiply(-2, 3))
        self.assertEqual(-6, self.calculator.multiply(2, -3))
        self.assertEqual(56, self.calculator.multiply(-8, -7))

    def test_division_identity(self):
        self.assertEqual(0, self.calculator.divide(0, 2))
        self.assertEqual(4, self.calculator.divide(4, 1))
        self.assertEqual(0.25, self.calculator.divide(1, 4))
        self.assertEqual(2.5, self.calculator.divide(5, 2))

    def test_division_of_negatives(self):
        self.assertEqual(0, self.calculator.divide(0, -2))
        self.assertEqual(-4, self.calculator.divide(4, -1))
        self.assertEqual(-0.25, self.calculator.divide(-1, 4))
        self.assertEqual(2.5, self.calculator.divide(-5, -2))

    def test_modulus_identity(self):
        self.assertEqual(0, self.calculator.modulus(0, 2))
        self.assertEqual(1, self.calculator.modulus(3, 2))
        self.assertEqual(2, self.calculator.modulus(2, 3))
        self.assertEqual(0, self.calculator.modulus(9, 3))

    def test_modulus_of_negatives(self):
        self.assertEqual(0, self.calculator.modulus(0, -2))
        self.assertEqual(1, self.calculator.modulus(-7, 2))
        self.assertEqual(-5, self.calculator.modulus(2, -7))
        self.assertEqual(-1, self.calculator.modulus(-5, -2))
        self.assertEqual(-2, self.calculator.modulus(-2, -5))

    def test_squared_identity(self):
        self.assertEqual(0, self.calculator.squared(0))
        self.assertEqual(4, self.calculator.squared(2))
        self.assertEqual(9, self.calculator.squared(3))
        self.assertEqual(25, self.calculator.squared(5))
        self.assertEqual(100, self.calculator.squared(10))

    def test_squared_of_negatives(self):
        self.assertEqual(4, self.calculator.squared(-2))
        self.assertEqual(9, self.calculator.squared(-3))
        self.assertEqual(25, self.calculator.squared(-5))
        self.assertEqual(100, self.calculator.squared(-10))

    def test_cubed_identity(self):
        self.assertEqual(0, self.calculator.cubed(0))
        self.assertEqual(1, self.calculator.cubed(1))
        self.assertEqual(8, self.calculator.cubed(2))
        self.assertEqual(27, self.calculator.cubed(3))
        self.assertEqual(64, self.calculator.cubed(4))
        self.assertEqual(1000, self.calculator.cubed(10))

    def test_cubed_of_negatives(self):
        self.assertEqual(-1, self.calculator.cubed(-1))
        self.assertEqual(-8, self.calculator.cubed(-2))
        self.assertEqual(-27, self.calculator.cubed(-3))
        self.assertEqual(-64, self.calculator.cubed(-4))
        self.assertEqual(-1000, self.calculator.cubed(-10))


if __name__ == '__main__':
    unittest.main()
