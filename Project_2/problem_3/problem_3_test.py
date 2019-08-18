import unittest
from Project_2.problem_3.problem_3 import HuffmanEncoding


class HuffmanEncodingTest(unittest.TestCase):
    def setUp(self):
        self.__h = HuffmanEncoding()

    def test_encoding(self):
        self.assertEqual(self.__h.h_encoding("Yadira"), "11001001011101")
        self.assertEqual(self.__h.h_encoding("Gato"), "10110001")
        self.assertEqual(self.__h.h_encoding("House"), "010011011110")
        # Encodes "Yadira" to binary as "11001001011101"
        print(self.__h.h_encoding("Yadira"))
        # Encodes "Gato" to binary as "10110001"
        print(self.__h.h_encoding("Gato"))
        # Encodes "House" to binary as "010011011110"
        print(self.__h.h_encoding("House"))

    def test_decoding(self):
        # Decodes binary "11001001011101" to YADIRA
        self.__h.h_encoding("YADIRA")
        self.assertEqual(self.__h.h_decoding("11001001011101"), "YADIRA")
        print(self.__h.h_decoding("11001001011101"))

    def test_encode_string_same_characters(self):
        self.__h.h_encoding("AAAAA")
        self.assertEqual(self.__h.h_encoding("AAAAA"), "00000")
        # Print "00000"
        print(self.__h.h_encoding("AAAAA"))

    def test_decode_string_same_characters(self):
        self.__h.h_encoding("AAAAA")
        self.assertEqual(self.__h.h_decoding("00000"), "AAAAA")
        # Print "AAAAA"
        print(self.__h.h_decoding("00000"))

    def test_encoding_empty(self):
        # if data y empty returns None
        self.assertIsNone(self.__h.h_encoding(""))
        print(self.__h.h_encoding(""))

    def test_decoding_empty(self):
        # if data y empty returns None
        self.assertIsNone(self.__h.h_decoding(""))
        print(self.__h.h_decoding(""))

    def test_encoding_node(self):
        # if data is None returns None
        self.assertIsNone(self.__h.h_encoding(None))
        print(self.__h.h_encoding(None))

    def test_decoding_node(self):
        # if data is None returns None
        self.assertIsNone(self.__h.h_decoding(None))
        print(self.__h.h_decoding(None))


if __name__ == '__main__':
    unittest.main()
