class KeyValue:
    # Constructor for KeyValue
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    # Defining comparision: return either a boolean value if your class knows how to compare itself to other
    # or NotImplemented if it does not
    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.key == other.key

    # To make a class hashable, it has to implement both __hash__(self) and __eq__(self, other). As with equality,
    # the inherited object.__hash__ method works by identity only: barring the unlikely event of a hash collision,
    # two instances of the same class will always have different hashes, no matter what data they carry
    def __hash__(self):
        return hash(self.key)

