import unittest
import copy
from Project_3.problem_4.problem_4 import sort_012


class Sort012Test(unittest.TestCase):
    def test_sort_case_1(self):
        array = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
        copy_array = copy.deepcopy(array)
        sort_012(copy_array)
        self.assertEqual(sorted(array), copy_array)

    def test_sort_case_2(self):
        array = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
        copy_array = copy.deepcopy(array)
        sort_012(copy_array)
        self.assertEqual(sorted(array), copy_array)

    def test_sort_case_3(self):
        array = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
        copy_array = copy.deepcopy(array)
        sort_012(copy_array)
        self.assertEqual(sorted(array), copy_array)

    def test_len_less_than_three_array(self):
        array = [0, 2, 1]
        copy_array = copy.deepcopy(array)
        sort_012(copy_array)
        self.assertEqual(sorted(array), copy_array)

    def test_none(self):
        self.assertIsNone(sort_012(None))

    def test_array_empty(self):
        self.assertIsNone(sort_012([]))

    def test_array_len_one(self):
        self.assertIsNone(sort_012([0]))

    def test_array_len_two(self):
        self.assertIsNone(sort_012([0, 1]))


if __name__ == '__main__':
    unittest.main()
