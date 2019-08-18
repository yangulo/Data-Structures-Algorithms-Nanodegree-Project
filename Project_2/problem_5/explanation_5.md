## Problem 5

* **Blockchain Implementation:**
    * A blockchain is a list of elements where each of them is a block. On this problem each block is an object of 
    type block. A block object contains a timestamp, a hash code (the timestamp and hash together make the block unique), 
    data and a previous_hash. The previous_hash is how the blocks are linked. A blockchain is very similar to a 
    linked list, therefore a linked list is implemented in this problem. Each new block is appended to the end of the 
    list and it is linked by its previous hash. 
* **Time and Space Efficiency:** 
    * A linked list organizes items sequentially, with each item storing a pointer to the next one. Each element of 
    a linked list (Node) is stored separately in memory, as opposite of arrays when the allocation of elements have 
    to be next to each other in memory, This makes storing in memory more flexible. However the space efficiency is 
    still O(n).
    * The time efficiency of searching, inserting and deleting items in a linked list is O(n). This makes a linked list 
    to have costly lookups, hence in order to search and update an item you have to walk from the head of the 
    linked list to the tail. However pre-appending (at the top) and appending (at the tail) are fast operations with 
    constant time O(1). This problem appends all new blocks at the tail, having a time efficiency of O(1). 