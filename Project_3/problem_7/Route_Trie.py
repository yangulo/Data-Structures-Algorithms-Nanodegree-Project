from Project_3.problem_7.Route_Trie_Node import RouterTrieNode


class RouteTrie:
    def __init__(self):
        self.root = RouterTrieNode()

    def insert(self, paths, handler):
        current = self.root
        for path in paths:
            if path not in current.children:
                current.insert(path)
            current = current.children[path]
        current.handler = handler

    def find(self, paths):
        node = self.root
        for path in paths:
            if path not in node.children:
                return None
            node = node.children[path]
        return node
