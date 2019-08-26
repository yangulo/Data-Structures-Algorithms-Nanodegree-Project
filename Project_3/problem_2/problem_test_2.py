import unittest
from Project_3.problem_2.problem_2 import rotated_array_search


class RotatedArraySearchTest(unittest.TestCase):

    def linear_search(self, input_list, number):
        for index, element in enumerate(input_list):
            if element == number:
                return index
        return -1

    def test_rotated_array_search_1(self):
        arr = [6, 7, 8, 9, 10, 1, 2, 3, 4]
        expected = self.linear_search(arr, 6)
        self.assertEqual(expected, rotated_array_search(arr, 6))
        print(rotated_array_search(arr, 6)) # Prints index 0

    def test_rotated_array_search_2(self):
        arr = [6, 7, 8, 9, 10, 1, 2, 3, 4]
        expected = self.linear_search(arr, 1)
        self.assertEqual(expected, rotated_array_search(arr, 1))
        print(rotated_array_search(arr, 1)) # Prints index 5

    def test_rotated_array_search_3(self):
        arr = [6, 7, 8, 1, 2, 3, 4]
        expected = self.linear_search(arr, 8)
        self.assertEqual(expected, rotated_array_search(arr, 8))
        print(rotated_array_search(arr, 8)) # Prints index 2

    def test_rotated_array_search_4(self):
        arr = [6, 7, 8, 1, 2, 3, 4]
        expected = self.linear_search(arr, 1)
        self.assertEqual(expected, rotated_array_search(arr, 1))
        print(rotated_array_search(arr, 1)) # Prints index 3

    def test_ordered_array_not_rotated(self):
        arr = [1, 2, 3, 4, 5]
        expected = self.linear_search(arr, 3)
        self.assertEqual(expected, rotated_array_search(arr, 3))
        print(rotated_array_search(arr, 3))  # Prints index 2

    def test_no_target_value_within_array(self):
        arr = [6, 7, 8, 1, 2, 3, 4]
        expected = self.linear_search(arr, 10)
        self.assertEqual(expected, rotated_array_search(arr, 10))
        print(rotated_array_search(arr, 10))  # Prints -1. No target value within array

    def test_none(self):
        self.assertIsNone(rotated_array_search(None, 10))
        print(rotated_array_search(None, 10))  # Prints None

    def test_empty_array(self):
        self.assertIsNone(rotated_array_search([], 10))
        print(rotated_array_search([], 10))  # Prints None


if __name__ == '__main__':
    unittest.main()

