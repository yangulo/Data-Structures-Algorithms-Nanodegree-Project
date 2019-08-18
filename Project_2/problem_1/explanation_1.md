## Problem 1:

* **LRC Implementation:** An LRC is built by combining two data structures, **a Double Linked list and a Hash Map**
    * A double Linked List will have the most-recently used item at the head of the list and the least-recently used 
    item at the tail. 
    * A Has Map; It will organize data so values can be quickly looked up given a unique key.
    * _LRU Logic:_ A cache is just fast storage. So its size is limited, for this project the max capacity is 5 
    elements. When the capacity is reached the LRU element is removed from the double linked list by removing the 
    element at the tail, and remove the same element from the hash map. This frees space on the cache and the a new 
    most recently used element could be added at the top of the list and also on the hash map. When requesting (get) 
    and element, that element is removed from its position first and then added at the top of the cache. When a new 
    element is added (set/put), then it is set at the top of the cache and saved in the hash map. When set/put an 
    existing element (based on a existing key), it is removed from its original position first, then moved at the top 
    of the list and its value gets updated. 

* **Time and Space Efficiency:**
    * The time accessing the LRU element is O(1) since it is at the tail of the linked list. 
    * The time inserting the most recent used element is O(1) since it will always be inserted at the top of the list
    * However, finding an item in a linked list is O(n), since the list needs to be walked to find an element, but 
    the point of building a cache is to have quick access. Therefore a Has Map data structured needs to be implemented. 
    The Hash Map will map items to linked list nodes so the time efficiency will be O(1)
    * The space Efficiency is heavy. An LRU cache tracking N items requires a linked list of length N, and a hash map 
    holding N items. That is s O(n) space, but it's still two data structures (as opposed to one).