import unittest
from Project_2.problem_1.KeyValue import KeyValue


class KeyValueTest(unittest.TestCase):
    def test_creation_key_value(self):
        key_value = KeyValue(1, 1)
        self.assertEqual(key_value.key, 1)
        self.assertEqual(key_value.value, 1)

    def test_creation_key_with_value_none(self):
        key_value = KeyValue(1)
        self.assertEqual(key_value.key, 1)
        self.assertEqual(key_value.value, None)

    def test_creation_key_value_as_none(self):
        key_value = KeyValue(None)
        self.assertIsNone(key_value.key, 1)


if __name__ == '__main__':
    unittest.main()
