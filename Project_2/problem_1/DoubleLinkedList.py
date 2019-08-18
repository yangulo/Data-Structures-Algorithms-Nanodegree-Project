from Project_2.problem_1.Node import Node


class DoubleLinkedList:
    # Constructor double LinkedList
    def __init__(self):
        self.head = None
        self.tail = None
        self.number_elements = 0
        return

    # Returns list size
    def size(self):
        return self.number_elements

    # Makes my class to be iterable (Iterate using for)
    def __iter__(self):
        next_element = self.head
        while next_element is not None:
            yield next_element.value
            next_element = next_element.next_value
        return

    # Inserts node at the beginning of the list
    def top_node(self, node):
        # Case 1 list is empty
        if self.head is None:
            self.head = node
            self.tail = node
            return

        # Case 2 list is not empty
        current_node = node
        current_node.next_value = self.head
        current_node.next_value.previous_value = current_node
        self.head = current_node
        return

    # removes a given node
    def remove_node(self, node):
        if self.head is None:
            return False

        # Case 1 node is at the beginning of the list
        if self.head == node:
            self.head = self.head.next_value
            return True

        # Case 2 node is at the end
        if self.tail == node:
            self.tail = node.previous_value
            self.tail.next_value = None
            return True

        # Case 3 node is in the middle
        current_value = node
        tmp_previous = current_value.previous_value
        tmp_next = current_value.next_value
        current_value.previous_value.next_value = tmp_next
        current_value.next_value.previous_value = tmp_previous
        return True

    # Add element at the beginning
    def top(self, value):
        # Case 1 list is empty. Add element at the beginning
        if self.head is None:
            self.head = Node(value)
            self.number_elements += 1
            return True

        # Case 2 list is not empty. Add element at the beginning
        current_node = Node(value)
        current_node.next_value = self.head
        current_node.next_value.previous_value = current_node
        self.head = current_node
        self.number_elements += 1
        # return "List: {0}, Value added on top: {1}".format(self.to_list(), value)
        return self.to_list()

    # Add element at the end
    def append(self, value):

        # TODO: Fix this along with remove line 123
        # Case 1 list is empty
        if self.head is None:  # and self.tail is None:
            node = Node(value)
            self.head = node
            self.tail = node
            self.number_elements += 1
            return True

        # Case 2 list is not empty. Add element at the end
        else:
            current_value = self.head
            new_node = Node(value)
            while current_value.next_value:
                current_value = current_value.next_value

            self.tail = current_value
            self.tail.next_value = new_node
            self.tail.next_value.previous_value = self.tail
            self.tail = new_node
            self.number_elements += 1
        return True

    # Remove element
    def remove_element(self, value):
        # Case 1 list is empty
        if self.head is None:
            return False

        # TODO: remove when one element in on the list head and tail are the same
        # Case 2 head value is equal value
        if self.head.value == value:
            self.head = self.head.next_value
            self.number_elements -= 1
            if self.number_elements == 0:
                self.tail = self.head
            return True

        current_value = self.head
        while current_value:
            # Case 3 value is in the end
            if current_value.next_value is None and current_value.value == value:
                value_removed = current_value.value
                self.tail = current_value.previous_value
                current_value.previous_value.next_value = None
                self.number_elements -= 1
                return True

            # Case 4 value is in the middle
            if current_value.value == value:
                value_removed = current_value.value
                tmp_previous = current_value.previous_value
                tmp_next = current_value.next_value
                current_value.previous_value.next_value = tmp_next
                current_value.next_value.previous_value = tmp_previous
                self.number_elements -= 1
                return True
            current_value = current_value.next_value
        # raise ValueError("Value not found in the list.")
        return False

    # Remove tail node and return it
    def pop_tail(self):
        # Case 1 remove tail
        if self.tail is not None and self.number_elements >= 0:
            value_removed = self.tail
            self.tail = self.tail.previous_value
            self.tail.next_value = None
            self.number_elements -= 1
            return value_removed
        # Case 2 do nothing, tail is none
        else:
            return False

    # Search element
    def search(self, value):
        # Case 1 head is none
        if self.head is None:
            return "Empty list"

        # Case 2 list is not empty
        current_value = self.head
        while current_value:
            if current_value.value == value:
                return True
            current_value = current_value.next_value
        return False

    # Create a list with values
    def to_list(self):
        out = list()
        for item in self.__iter__():
            out.append(item)
        return out

