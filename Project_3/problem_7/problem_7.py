from Project_3.problem_7.Route_Trie import RouteTrie


class Router:
    def __init__(self, root_handler, error_handler):
        self.error_handler = error_handler
        self.trie = RouteTrie()
        self.trie.insert(self.split_path("/"), root_handler)

    def add_handler(self, path, handler):
        array = self.split_path(path)
        self.trie.insert(array, handler)

    def lookup(self, path):
        if path is None:
            return None
        array = self.split_path(path)
        if array is not None:
            node = self.trie.find(array)
            if node is not None and node.handler is not None:
                return node.handler
        return self.error_handler

    def split_path(self, path):
        if path and len(path.strip()) > 0:
            return path.strip().replace('/', ' ').rstrip().split(' ')
        return None


