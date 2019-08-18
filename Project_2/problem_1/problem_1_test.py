import unittest
from Project_2.problem_1.problem_1 import LRUCache


class LRUCacheTest(unittest.TestCase):
    def setUp(self):
        self.__cache = LRUCache()
        self.__tmp = self.__cache.get_dll()

    def test_set_value_cache(self):
        self.assertTrue(self.__cache.set(1, "Yadira"))
        # Set on top. Sets "Edgar" on top
        self.assertTrue(self.__cache.set(9, "Edgar"))
        self.assertEqual(self.__tmp.to_list(), ["Edgar", "Yadira"])
        # Prints cache["Edgar", "Yadira"]
        print(self.__tmp.to_list())

    def test_set_value_existing_key(self):
        self.__cache.set(2, 2)
        self.__cache.set(1, 1)
        self.__cache.set(3, 3)
        self.__cache.set(1, 10)
        print(self.__cache.get(1))
        # should return 10
        print(self.__cache.get(2))
        # should return 2
        self.__cache.set(1, "Carmen")
        print(self.__cache.get(1))

    def test_max_capacity_cache(self):
        self.__cache.set(1, 1)
        self.__cache.set(2, 2)
        self.__cache.set(3, 3)
        self.__cache.set(4, 4)

        print(self.__cache.get(1))
        # returns 1
        print(self.__cache.get(2))
        # returns 2
        print(self.__cache.get(9))
        # returns -1 because 9 is not present in the cache

        self.__cache.set(5, 5)
        # Max capacity. Remove LRU to add 6
        self.__cache.set(6, 6)
        # returns 6
        print(self.__cache.get(6))
        # prints capacity 5
        print(self.__cache.number_elements)
        # should return -1
        print(self.__cache.get(3))

    def test_set_none(self):
        # Values as None, asserts False
        self.assertFalse(self.__cache.set(None, None))
        # return False for None values
        print(self.__cache.set(None, None))
        self.assertFalse(self.__cache.set(0, None))
        # return False, if at least one value is None
        print(self.__cache.set(0, None))
        self.assertFalse(self.__cache.set(None, 0))
        # return False, if at least one value is None
        print(self.__cache.set(None, 0))

    def test_set_zero_capacity(self):
        new_cache = LRUCache(0)
        self.assertEqual(new_cache.set(1, 1), "Can't perform operations on 0 capacity cache")
        print(new_cache.set(1, 1))

    def test_get_existing_value(self):
        self.__cache.set(1, "Yadira")
        self.__cache.set(9, "Edgar")
        self.assertEqual(self.__cache.get(1), "Yadira")
        # prints Yadira
        print(self.__cache.get(1))

        # Setting existing value to top
        self.__cache.get(1)
        self.assertEqual(self.__tmp.to_list(), ["Yadira", "Edgar"])
        # Existing value "Yadira" on top of cache. Prints ["Yadira", "Edgar"]
        print(self.__cache.get_dll().to_list())

    def test_get_non_existing_value(self):
        self.__cache.set(1, 1)
        self.__cache.set(2, 2)
        self.assertEqual(self.__cache.get(10), -1)
        # Prints -1 for a non existing value
        print(self.__cache.get(10))
        print(self.__cache.get(20))

    def test_get_none(self):
        # Key is None
        self.assertFalse(self.__cache.get(None))
        # Print False when key is None
        print(self.__cache.get(None))

    def test_get_value_zero_capacity_cache(self):
        new_cache = LRUCache(0)
        new_cache.set(1, 1)
        # prints -1, no key will be found on 0 capacity cache
        self.assertEqual(new_cache.get(1), -1)
        print(new_cache.get(1))


if __name__ == '__main__':
    unittest.main()
