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

    def test_power_identity(self):
        self.assertEqual(1, self.calculator.power(1, 4))
        self.assertEqual(4, self.calculator.power(2, 2))
        self.assertEqual(27, self.calculator.power(3, 3))
        self.assertEqual(256, self.calculator.power(4, 4))
        self.assertEqual(3125, self.calculator.power(5, 5))

    def test_power_of_negatives(self):
        self.assertEqual(-1, self.calculator.power(-1, 1))
        self.assertEqual(4, self.calculator.power(-2, 2))
        self.assertEqual(-27, self.calculator.power(-3, 3))
        self.assertEqual(256, self.calculator.power(-4, 4))
        self.assertEqual(-3125, self.calculator.power(-5, 5))

    def test_sqrt_identity(self):
        self.assertEqual(0, self.calculator.sqrt(0))
        self.assertEqual(1, self.calculator.sqrt(1))
        self.assertEqual(2, self.calculator.sqrt(4))
        self.assertEqual(3, self.calculator.sqrt(9))
        self.assertEqual(4, self.calculator.sqrt(16))
        self.assertEqual(5, self.calculator.sqrt(25))
        self.assertEqual(10, self.calculator.sqrt(100))

    def test_sqrt_of_negatives(self):
        self.assertEqual(1.2246467991473532e-16+2j, self.calculator.sqrt(-4))
        self.assertEqual(1.8369701987210297e-16+3j, self.calculator.sqrt(-9))
        self.assertEqual(2.4492935982947064e-16+4j, self.calculator.sqrt(-16))
        self.assertEqual(3.061616997868383e-16+5j, self.calculator.sqrt(-25))
        self.assertEqual(6.123233995736766e-16+10j, self.calculator.sqrt(-100))

    def test_root_identity(self):
        self.assertEqual(1, self.calculator.root(1, 1))
        self.assertEqual(2, self.calculator.root(4, 2))
        self.assertEqual(2, self.calculator.root(8, 3))
        self.assertEqual(3, self.calculator.root(9, 2))
        self.assertEqual(3, self.calculator.root(27, 3))
        self.assertEqual(3, self.calculator.root(81, 4))
        self.assertEqual(3, self.calculator.root(243, 5))

    def test_abs_identity(self):
        self.assertEqual(1, self.calculator.abs(1))
        self.assertEqual(1.345, self.calculator.abs(1.345))
        self.assertEqual(1234, self.calculator.abs(1234))
        self.assertEqual(2, self.calculator.abs(-2))
        self.assertEqual(3.45, self.calculator.abs(-3.45))


if __name__ == '__main__':
    unittest.main()
