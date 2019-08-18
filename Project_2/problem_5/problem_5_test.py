import unittest
from Project_2.problem_5.problem_5 import Blockchain


class BlockchainTest(unittest.TestCase):
    def setUp(self):
        self.__b = Blockchain()

    def test_create_blockchain(self):
        # Adding blocks
        self.assertTrue(self.__b.add_element("Yadira"))
        self.assertTrue(self.__b.add_element("Edgar"))
        self.assertTrue(self.__b.add_element("Carmen"))
        self.assertTrue(self.__b.add_element("Carlos"))

        print(self.__b)

    def test_empty_blockchain(self):
        self.assertTrue(self.__b.is_empty())
        # Prints True since blockchain is empty
        print(self.__b.is_empty())

    def test_not_empty_blochain(self):
        self.__b.add_element("Yadira")
        self.assertFalse(self.__b.is_empty())
        # Prints false since blockchain is not empty
        print(self.__b.is_empty())

    def test_data_none(self):
        # None value
        self.assertFalse(self.__b.add_element(None))
        # Prints False for None values
        print(self.__b.add_element(None))

    def test_data_empty(self):
        # Empty value
        self.assertFalse(self.__b.add_element(""))
        # Prints False for None and empty values
        print(self.__b.add_element(""))


if __name__ == '__main__':
    unittest.main()
