import unittest

from awesome_application import Calculator


class UnitTests(unittest.TestCase):

    # Slightly better tests, checking both valid and invalid cases
    # and more than one example per valid/invalid path
    def test_valid_addition(self):
        # (x, y, answer)
        test_cases = [
            (2, 2, 4),
            (10, 0, 10),
            (-3, 6, 3),
        ]

        for test_case in test_cases:
            x, y, answer = test_case
            self.assertEqual(Calculator.addition(x, y), answer)

    def test_invalid_addition(self):
        # (x, y, answer)
        test_cases = [
            (2, 2, 5),
            (10, 0, 20),
        ]

        for test_case in test_cases:
            x, y, answer = test_case
            self.assertNotEqual(Calculator.addition(x, y), answer)


if __name__ == '__main__':
    unittest.main()
