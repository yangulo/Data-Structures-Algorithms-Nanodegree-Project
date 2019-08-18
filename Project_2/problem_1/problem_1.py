from Project_2.problem_1.Node import Node
from Project_2.problem_1.DoubleLinkedList import DoubleLinkedList
from Project_2.problem_1.HashMap import HashMap


class LRUCache(object):
    # Constructor last recent used
    def __init__(self, capacity=5):
        # Initialize class variables
        self.capacity = capacity
        self.number_elements = 0
        self.__has_map = HashMap(capacity)
        self.__dll = DoubleLinkedList()

    def get_dll(self):
        return self.__dll

    # Get item, and add it at the top of the linkedlist as most recent used
    def get(self, key):
        if key is None:
            return False
        # Retrieve item from provided key. Return -1 if nonexistent.
        # Case 1 element exists
        if self.__has_map.get(key):
            new_element = self.__has_map.get(key)
            self.__dll.remove_node(new_element)
            self.__dll.top_node(new_element)
            return new_element.value
        # Case 2 element does not exists
        else:
            return -1

    # Add a value
    def set(self, key, value):
        if key is None or value is None:
            return False
        # Set the value if the key is not present in the problem_1. If the problem_1 is at capacity
        # remove the oldest item.
        # Case 1 number of elements less than capacity
        if self.number_elements < self.capacity:
            # Case 1 key does not exist
            if self.__has_map.get(key) is None:
                node = Node(value)
                node.key = key
                self.__has_map.put(key, node)
                self.__dll.top_node(node)
            # Case 2 key exists
            else:
                node = self.__has_map.get(key)
                node.value = value
                self.__dll.remove_node(node)
                self.__dll.top_node(node)
            self.number_elements += 1
            return True

        # Case 2 need to remove an element cause the problem_1 is full
        else:
            value_removed = self.__dll.pop_tail()
            self.__has_map.remove_element(value_removed.key)
            self.number_elements -= 1
            return self.set(key, value)

