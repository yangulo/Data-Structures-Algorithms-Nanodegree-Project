import unittest
from Project_2.problem_1.DoubleLinkedList import DoubleLinkedList
from Project_2.problem_6.problem_6 import intersection


class IntersectionTest(unittest.TestCase):
    def setUp(self):
        self.__dll_1 = DoubleLinkedList()
        self.__dll_2 = DoubleLinkedList()
        for element in range(10, 16):
            self.__dll_1.append(element)
        for element in range(10, 13):
            self.__dll_2.append(element)

    def test_intersection(self):
        i_dll = intersection(self.__dll_1, self.__dll_2)

        # Returns only the intersection of numbers within the two lists
        self.assertEqual(i_dll.to_list(), [10, 11, 12])
        # Print [10, 11, 12]
        print(i_dll.to_list())

        # Adding elements doesn't affect it
        self.__dll_2.append(30)
        self.__dll_1.append(33)
        self.assertEqual(i_dll.to_list(), [10, 11, 12])
        print(i_dll.to_list())

    def test_empty_lists(self):
        dll_1 = DoubleLinkedList()
        dll_2 = DoubleLinkedList()

        # Empty lists, there is no intersection. Returns None
        self.assertIsNone(intersection(dll_1, dll_2))
        print(intersection(dll_1, dll_2))

        # None input, returns None
        self.assertIsNone(intersection(None, None))
        print(intersection(None, None))

        # If one list is empty there is no intersection. Returns None
        self.assertIsNone(intersection(dll_1, self.__dll_2))
        self.assertIsNone(intersection(self.__dll_1, dll_2))
        print(intersection(dll_1, self.__dll_2))
        print(intersection(self.__dll_1, dll_2))

        # if one list is None there is no intersection. Returns None
        self.assertIsNone(intersection(None, self.__dll_2))
        self.assertIsNone(intersection(self.__dll_1, None))
        print(intersection(None, self.__dll_2))
        print(intersection(self.__dll_1, None))


if __name__ == '__main__':
    unittest.main()
