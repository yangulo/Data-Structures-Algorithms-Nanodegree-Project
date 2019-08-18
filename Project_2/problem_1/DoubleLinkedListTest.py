import unittest
from Project_2.problem_1.DoubleLinkedList import DoubleLinkedList
from Project_2.problem_1.Node import Node


class DoubleLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.__value = 2
        self.__node = Node(1)
        self.__dll = DoubleLinkedList()

    def test_append_dll(self):
        # Empty list
        self.assertTrue(self.__dll.append(self.__value))
        # Not empty list
        self.assertTrue(self.__dll.append(self.__value))

    def test_size_dll(self):
        self.__dll.append(self.__value)
        self.assertEqual(self.__dll.size(), 1)

    def test_top_dll(self):
        self.__dll.append(self.__value)
        self.assertTrue(self.__dll.top(1))

    def test_top_node_dll(self):
        self.__dll.head = self.__node
        self.__dll.tail = self.__node
        self.__dll.top_node(Node(0))
        self.assertEqual(self.__dll.head.value, 0)
        self.assertEqual(self.__dll.tail.value, 1)

        self.__dll.top_node(Node(5))
        self.assertEqual(self.__dll.head.value, 5)
        self.assertEqual(self.__dll.tail.value, 1)

    def test_remove_element(self):
        self.__dll.append(5)
        self.__dll.append(6)

        # Remove head
        self.assertTrue(self.__dll.remove_element(5))

        # Remove tail
        self.assertTrue(self.__dll.remove_element(6))

        # Remove middle value
        for element in range(5, 8):
            self.__dll.append(element)
        self.assertTrue(self.__dll.remove_element(6))

    def test_remove_node(self):
        self.__dll.top_node(self.__node)
        self.__dll.top_node(Node(self.__value))

        # Remove head
        self.assertTrue(self.__dll.remove_node(self.__node))

        # Remove tail
        self.__dll.remove_element(2)
        self.__dll.top_node(self.__node)
        self.__dll.append(self.__value)
        self.assertTrue(self.__dll.remove_node(self.__node))

        # Remove middle
        self.__dll.remove_element(2)
        self.__dll.append(1)
        self.__dll.top_node(self.__node)
        self.__dll.top(0)
        self.assertTrue(self.__dll.remove_node(self.__node))

    def test_pop_tail(self):
        for element in range(0, 2):
            self.__dll.append(element)
        self.assertTrue(self.__dll.pop_tail())
        self.__dll.remove_element(0)
        # No elements to removed. Empty dll
        self.assertFalse(self.__dll.pop_tail(), False)

    def test_search(self):
        self.__dll.append(self.__value)
        # Search existing element
        self.assertTrue(self.__dll.search(2))
        # Search non existing element
        self.assertFalse(self.__dll.search(9))
        # Search null in list
        self.assertFalse(self.__dll.search(None))

    def test_to_list(self):
        for element in range(0, 3):
            self.__dll.append(element)
        self.assertEqual(self.__dll.to_list(), [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
