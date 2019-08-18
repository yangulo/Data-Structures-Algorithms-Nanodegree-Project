from Project_2.problem_1.DoubleLinkedList import DoubleLinkedList
from Project_2.problem_1.KeyValue import KeyValue


class HashMap:
    # Constructor of the hash map
    def __init__(self, initial_size=10):
        self.bucket = [DoubleLinkedList() for _ in range(initial_size)]
        self.prime = 123
        self.num_entries = 0

    # Find which linkedlist to use in the array
    def __find_key(self, key):
        bucket_index = self.get_bucket_index(key)
        dll = self.bucket[bucket_index]

        # Iterate linkedlist and return node
        for element in dll:
            if element.key == key:
                return element
        return None

    # Add element
    def put(self, key, value):
        if key is None:
            return False
        kv = self.__find_key(key)

        # Case 1 node exists in list, replace value
        if kv is not None:
            kv.value = value

        # Case 2 element does not exists in list, add value
        else:
            bucket_index = self.get_bucket_index(key)
            dll = self.bucket[bucket_index]
            dll.append(KeyValue(key, value))
            self.num_entries += 1
        return True

    # Get element within hashmap
    def get(self, key):
        if key is None:
            return None
        kv = self.__find_key(key)
        if kv is not None:
            return kv.value
        return None

    # Size of the list
    def size(self):
        return self.num_entries

    # Remove node from list and hashmap
    def remove_element(self, key):
        if key is None:
            return False
        bucket_index = self.get_bucket_index(key)
        dll = self.bucket[bucket_index]
        return dll.remove_element(KeyValue(key))

    # Get bucket index
    def get_bucket_index(self, key):
        if key is None:
            return False
        bucket_index = self.hash_function(key)
        return bucket_index

    # Create hash code
    def hash_function(self, key):
        if key is None:
            return False
        # (prime * key/2^(w-m)) % num_entries (Refer Wikipedia)
        #hv = ((self.prime * key) / 2 ^ 4) % len(self.bucket)
        return hash(key) % len(self.bucket)



