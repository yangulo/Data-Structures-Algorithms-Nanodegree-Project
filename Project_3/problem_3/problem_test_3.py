import unittest
from Project_3.problem_3.problem_3 import rearrange_digits


class RearrangeDigits(unittest.TestCase):
    def test_rearrange(self):
        self.assertEqual(rearrange_digits([1, 2, 3, 4, 5]), [531, 42])
        self.assertEqual(rearrange_digits([4, 6, 2, 5, 9, 8]), [964, 852])

        print(rearrange_digits([1, 2, 3, 4, 5]))     # Prints [531, 42]
        print(rearrange_digits([4, 6, 2, 5, 9, 8]))  # Prints [964, 852]

    def test_array_len_1(self):
        self.assertIsNone(rearrange_digits([9]))
        print(rearrange_digits([9])) # Prints None. Hence an array of one element wont form two numbers

    def test_empty(self):
        self.assertIsNone(rearrange_digits([]))
        print(rearrange_digits([]))  # Prints None. Hence an empty array wont form two numbers

    def test_null(self):
        self.assertIsNone(rearrange_digits([None]))
        print(rearrange_digits([9]))  # Prints None


if __name__ == '__main__':
    unittest.main()
