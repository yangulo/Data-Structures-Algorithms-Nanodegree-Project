import unittest
from Project_3.problem_1.problem_1 import sqrt


class SqrtTest(unittest.TestCase):
    def test_find_sqrt(self):
        self.assertEqual(sqrt(27), 5)
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(16), 4)
        self.assertEqual(sqrt(1), 1)
        self.assertEqual(sqrt(0), 0)

        print(sqrt(27)) # Prints 5
        print(sqrt(9))  # Prints 3
        print(sqrt(16)) # Prints 4
        print(sqrt(1))  # Prints 1
        print(sqrt(0))  # Prints 0

    def test_float_sqrt(self):
        self.assertEqual(sqrt(27.9), 5)
        print(sqrt(27.9)) # Prints 5

    def test_sqrt_null(self):
        self.assertIsNone(sqrt(None))
        print(sqrt(None)) # Prints None

    def test_sqrt_string(self):
        self.assertIsNone(sqrt("9"))
        print(sqrt("9"))  # Prints None


if __name__ == '__main__':
    unittest.main()
