import unittest
from Project_2.problem_1.problem_1 import LRUCache


class LRUCacheTest(unittest.TestCase):
    def setUp(self):
        self.__cache = LRUCache()
        self.__tmp = self.__cache.get_dll()

    def test_set_value_cache(self):
        # Set empty cache. Sets "Yadira"
        self.assertTrue(self.__cache.set(1, "Yadira"))
        # Set on top. Sets "Edgar" on top
        self.assertTrue(self.__cache.set(9, "Edgar"))

        # Tests asserts equal ["Edgar", "Yadira"]
        self.assertEqual(self.__tmp.to_list(), ["Edgar", "Yadira"])
        # Prints cache["Edgar", "Yadira"]
        print(self.__tmp.to_list())

        # Update value and place on top
        self.__cache.set(1, "Carmen")
        self.assertEqual(self.__cache.get(1), "Carmen")

        # Tests asserts equal ["Carmen", "Edgar"]
        self.assertEqual(self.__tmp.to_list(), ["Carmen", "Edgar"])
        # Print updated cache ["Carmen", "Edgar"]
        print(self.__tmp.to_list())

        # Values as None, asserts False
        self.assertFalse(self.__cache.set(None, None))
        self.assertFalse(self.__cache.set(0, None))
        self.assertFalse(self.__cache.set(None, 0))

    def test_get_value_cache(self):
        self.__cache.set(1, "Yadira")

        # Existing value
        self.assertEqual(self.__cache.get(1), "Yadira")
        # Print existing value Yadira
        print(self.__cache.get(1))

        # Not existing value
        self.assertEqual(self.__cache.get(10), -1)
        # Prints -1 for a non existing value
        print(self.__cache.get(10))

        # Existing cache ['Edgar', 'Yadira']
        self.__cache.set(9, "Edgar")
        print(self.__cache.get_dll().to_list())
        # Setting existing value to top
        self.__cache.get(1)
        self.assertEqual(self.__tmp.to_list(), ["Yadira", "Edgar"])
        # Existing value "Yadira" on top of cache. Prints ["Yadira", "Edgar"]
        print(self.__cache.get_dll().to_list())

        # Key is None
        self.assertFalse(self.__cache.get(None))


if __name__ == '__main__':
    unittest.main()
