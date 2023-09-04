import unittest

from awesome_application import Calculator

from hypothesis import given
from hypothesis.strategies import integers


class UnitTests(unittest.TestCase):
    @given(x=integers(), y=integers())
    def test_division(self, x, y):
        self.assertEqual(Calculator.division(x, y), x / y)

    @given(x=integers(), y=integers())
    def test_division(self, x, y):
        self.assertEqual(Calculator.division(x, y), x / y)


if __name__ == '__main__':
    unittest.main()
