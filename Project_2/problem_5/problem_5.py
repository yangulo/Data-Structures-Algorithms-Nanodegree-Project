from Project_2.problem_1.DoubleLinkedList import DoubleLinkedList
from Project_2.problem_5.Block import Block


class Blockchain:
    def __init__(self):
        self.__dll = DoubleLinkedList()
        self.__last_block = None

    def is_empty(self):
        return self.__dll.size() == 0

    def add_element(self, data):
        # Data is None
        if data is None or len(data) == 0:
            return False
        # linked list is empty
        if self.__dll.head is None:
            new_block = Block(data, 0)
            self.__last_block = new_block
            self.__dll.append(new_block)
            return True
        # linked list is not empty
        else:
            new_block = Block(data, self.__last_block.hash)
            self.__last_block = new_block
            self.__dll.append(new_block)
            return True

    def __iter__(self):
        for item in self.__dll:
            yield item

    def __repr__(self):
        return "\n".join(str(x) for x in self.__iter__())

