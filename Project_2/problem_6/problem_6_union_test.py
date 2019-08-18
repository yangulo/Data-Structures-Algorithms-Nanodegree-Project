import unittest
from Project_2.problem_1.DoubleLinkedList import DoubleLinkedList
from Project_2.problem_6.problem_6 import union


class UnionTest(unittest.TestCase):
    def setUp(self):
        self.__dll_1 = DoubleLinkedList()
        self.__dll_2 = DoubleLinkedList()
        for element in range(0, 4):
            self.__dll_1.top(element)
        for element in range(4, 7):
            self.__dll_2.top(element)

    def test_union(self):
        u_dll = union(self.__dll_1, self.__dll_2)
        self.assertEqual(u_dll.to_list(), [6, 5, 4, 3, 2, 1, 0])

        # Print union linked list [6, 5, 4, 3, 2, 1, 0]
        print(u_dll.to_list())

    def test_union_empty_ll(self):
        dll_1 = DoubleLinkedList()
        dll_2 = DoubleLinkedList()
        u_dll = union(dll_1, dll_2)

        # Empty linked list. returns empty list
        self.assertEqual(u_dll.to_list(), [])
        print(u_dll.to_list())

        # Linked lists are None
        self.assertIsNone(union(None, None))
        print(union(None, None))


if __name__ == '__main__':
    unittest.main()
