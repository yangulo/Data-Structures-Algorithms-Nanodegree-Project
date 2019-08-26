import unittest
from Project_3.problem_6.problem_6 import get_min_max


class GetMinMax(unittest.TestCase):
    def test_get_min_max(self):
        self.assertEqual(get_min_max([2, 10, 9, 20, 30, 5, 0, 31, 100]), (0, 100))
        print(get_min_max([2, 10, 9, 20, 30, 5, 0, 31, 100]))   # Prints 0, 100

    def test_get_max_min_negative_num(self):
        self.assertEqual(get_min_max([2, 10, 9, 20, 30, 5, 0, 31, -100]), (-100, 31))
        print(get_min_max([2, 10, 9, 20, 30, 5, 0, 31, -100]))  # Prints -100, 31

    def test_get_max_min_none(self):
        self.assertIsNone(get_min_max(None))
        print(get_min_max(None))  # Prints None

    def test_get_max_min_empty(self):
        self.assertIsNone(get_min_max([]))
        print(get_min_max([]))  # Prints None, empty array

    def test_one_element_array(self):
        self.assertIsNone(get_min_max([100]))
        print(get_min_max([100]))  # Prints None. Hence one element array can't be max and min number


if __name__ == '__main__':
    unittest.main()
