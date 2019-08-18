import unittest
from Project_2.problem_1.HashMap import HashMap


class HashMapTest(unittest.TestCase):
    def setUp(self):
        self.__hm = HashMap()
        self.__key = 1

    def test_put__hm(self):
        # Value doesn't exist in map
        self.assertEqual(self.__hm.put(1, 1), True)
        # Replace existing value
        self.__hm.put(1, 10)
        self.assertEqual(self.__hm.get(1), 10)
        # Key does not exists key equal to None
        self.assertFalse(self.__hm.put(None, 1))

    def test_get_hm(self):
        self.__hm.put(1, 1)
        # Key exists
        self.assertEqual(self.__hm.get(1), 1)
        # Key does not exists
        self.assertFalse(self.__hm.get(10))
        # key is None
        self.assertFalse(self.__hm.get(None))

    def test_size_hm(self):
        self.__hm.put(1, 1)
        self.assertEqual(self.__hm.size(), 1)

    def test_remove_element(self):
        for element in range(0, 11):
            self.__hm.put(self.__key, element)
            self.__key += 1
        # Key exists
        self.assertTrue(self.__hm.remove_element(1))
        # Key does not exists
        self.assertFalse(self.__hm.remove_element(20))
        # Key is None
        self.assertFalse(self.__hm.remove_element(None))


if __name__ == '__main__':
    unittest.main()
