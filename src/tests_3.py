import unittest

from awesome_application import Calculator

from hypothesis import given
from hypothesis.strategies import integers


class UnitTests(unittest.TestCase):

    # Now we're testing random values which is great, but we're testing with the implementation!
    # What if there is a bug with the implementation?
    @given(x=integers(), y=integers())
    def test_addition(self, x, y):
        self.assertEqual(Calculator.addition(x, y), x + y)


if __name__ == '__main__':
    unittest.main()
