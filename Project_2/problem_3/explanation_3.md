## Problem 3

* **Huffman Code Implementation:** a Huffman code is a particular type of optimal prefix code that is commonly used for 
lossless data compression.
    * There are mainly two major parts in Huffman Coding
        * Build a Huffman Tree from input characters.
        * Traverse the Huffman Tree and assign codes to characters.
* **Time and Space Efficiency:**
    * Searching a binary tree with n nodes has a minimum of O(log n) levels, it takes at least O(log n) comparisons to 
    find a particular node. A binary tree is implemented in the Huffman encoding problem.
    * The time complexity of the Huffman algorithm is O(n log n). For every encoded symbol you have to traverse the 
    tree in order to decode that symbol. The tree contains N nodes and, on average, it takes O(log n) node visits to 
    decode a symbol. So the time complexity would be O(n log n).
    * Space complexity is O(n) for the tree and O(n) for the decoded text.