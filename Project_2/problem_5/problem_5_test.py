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

        # print(self.__b) -> Prints whole blockchain
        # Print each block previous hash.
        for block in self.__b:
            # Print previous and current hash. Previous hash for first block is 0, while previous hash for following
            # blocks is the current hash of the previous block
            print("New Block")
            print("Previous hash: ", block.previous_hash)
            print("Current has: ", block.hash)

    def test_data_none(self):
        # None and empty value
        self.assertFalse(self.__b.add_element(None))
        self.assertFalse(self.__b.add_element(""))

        # Prints False for None and empty values
        print(self.__b.add_element(None))
        print(self.__b.add_element(""))


if __name__ == '__main__':
    unittest.main()
