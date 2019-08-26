class RouterTrieNode:
    def __init__(self):
        self.handler = None
        self.children = {}

    def insert(self, path):
        self.children[path] = RouterTrieNode()
