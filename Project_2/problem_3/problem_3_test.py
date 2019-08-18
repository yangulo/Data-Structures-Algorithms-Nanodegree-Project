import unittest
from Project_2.problem_3.problem_3 import HuffmanEncoding


class HuffmanEncodingTest(unittest.TestCase):
    def setUp(self):
        self.__h = HuffmanEncoding()

    def test_encoding_decoding(self):
        # Encodes "Yadira" to binary as "11001001011101"
        self.assertEqual(self.__h.h_encoding("Yadira"), "11001001011101")
        print(self.__h.h_encoding("Yadira"))

        # Decodes binary "11001001011101" as "YADIRA"
        self.assertEqual(self.__h.h_decoding("11001001011101"), "YADIRA")
        print(self.__h.h_decoding("11001001011101"))

    def test_encoding_decoding_empty(self):
        # if data y empty returns None
        self.assertIsNone(self.__h.h_encoding(""))
        self.assertIsNone(self.__h.h_decoding(""))
        print(self.__h.h_encoding(""))
        print(self.__h.h_decoding(""))

    def test_encoding_decoding_node(self):
        # if data is None returns None
        self.assertIsNone(self.__h.h_encoding(None))
        self.assertIsNone(self.__h.h_decoding(None))
        print(self.__h.h_encoding(None))
        print(self.__h.h_decoding(None))


if __name__ == '__main__':
    unittest.main()
