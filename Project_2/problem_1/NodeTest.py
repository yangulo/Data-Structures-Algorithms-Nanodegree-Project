import unittest
from Project_2.problem_1.Node import Node


class NodeTestCase(unittest.TestCase):

    def test_create_node(self):
        node = Node(5)
        self.assertEqual(node.value, 5)
        self.assertIsNone(node.key)
        self.assertIsNone(node.next_value)
        self.assertIsNone(node.previous_value)

    def test_create_node_with_none(self):
        node = Node(None)
        self.assertIsNone(node.value)
        self.assertIsNone(node.key)
        self.assertIsNone(node.next_value)
        self.assertIsNone(node.previous_value)

    def test_create_node_with_no_value(self):
        with self.assertRaises(Exception) as context:
            node = Node()

        # The message should be the same as the exception above
        self.assertTrue('__init__() takes exactly 2 arguments (1 given)' in context.exception)


if __name__ == '__main__':
    unittest.main()
