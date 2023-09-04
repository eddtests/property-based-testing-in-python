import unittest

from awesome_application import Calculator


class UnitTests(unittest.TestCase):

    # Simple happy path test, the most common type found in the wild
    # What if Calculator.addition(x, y) => x * y?
    def test_addition(self):
        result = Calculator.addition(2, 2)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
