# Problem 5:

## Description
* This problem is about implementing an autocomplete algorithm using a trie approach and an interactive search box to see 
that correct autocomplete words are returned

## Implementation
* For this problem solution a trie data structure is implemented together with a trie node  and a suffixes function to be able 
to provide the suffixes (autocomplete words given for a given prefix provided by the user). This prefix will be search within 
the Trie returning a given TrieNode. This node is used to recursively retrieve all possible suffixes within it and then saved in an array
so that this array can be returned with all possible words.

## Complexity
* The space complexity of this problem is O(n). Each node within a trie is saved in memory. Therefore (n) nodes in a dictionary 
of size (m) has space complexity of O(MN) which approximates to O(n)
* The time complexity of this solution is O(n) which means the time complexity of inserting a words (each character of a word) 
in the trie of size (m), given a complexity of O(m*n) which approximates to O(n)