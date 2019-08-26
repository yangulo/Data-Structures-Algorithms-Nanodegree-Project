from Project_3.helpers.Trie_Node import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.insert(char)
            current = current.children[char]
        current.is_word = True

    def find(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]
        return current


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

trie_node = MyTrie.find('f')
suffix = list()
print(trie_node.suffixes(suffix))
print(suffix)
