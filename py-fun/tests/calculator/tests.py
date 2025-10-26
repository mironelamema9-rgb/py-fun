import unittest
from src.calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # This runs before each test method
        self.calc = Calculator()

    def test_add_numbers(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_strings(self):
        # Assuming your add can parse strings representing numbers
        self.assertEqual(self.calc.add("3", "4"), 7)

    def test_factorize(self):
        # Test the factorize method
        self.assertEqual(self.calc.factorize(28), [2, 2, 7])

if __name__ == "__main__":
    unittest.main()