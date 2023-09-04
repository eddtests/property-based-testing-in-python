import unittest

from awesome_application import Calculator

from hypothesis import given
from hypothesis.strategies import integers


class UnitTests(unittest.TestCase):

    # Testing the properties, or behavior, of addition! :D
    @given(x=integers(), y=integers())
    def test_addition_is_commutative(self, x, y):
        self.assertEqual(Calculator.addition(x, y), Calculator.addition(y, x))

    @given(x=integers(), y=integers(), z=integers())
    def test_addition_is_associative(self, x, y, z):
        self.assertEqual(
            Calculator.addition(Calculator.addition(x, y), z),
            Calculator.addition(x, Calculator.addition(y, z))
        )

    @given(x=integers())
    def test_addition_identity_function(self, x):
        self.assertEqual(Calculator.addition(x, 0), x)

    @given(x=integers())
    def test_addition_inverse(self, x):
        self.assertEqual(Calculator.addition(x, -x), 0)


if __name__ == '__main__':
    unittest.main()
