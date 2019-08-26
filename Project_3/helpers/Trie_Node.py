class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, char):
        self.children[char] = TrieNode()

    def suffixes(self, suffix, word=''):
        for key in self.children:
            node = self.children[key]
            if node.is_word:
                suffix.append(word + key)
            node.suffixes(suffix, word + key)
        return

