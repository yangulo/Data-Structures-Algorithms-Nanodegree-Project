import hashlib
from datetime import datetime


class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.utcnow()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    # To print an object as a string
    def __repr__(self):
        return "{} {} {} {}".format(self.timestamp, self.data, self.previous_hash, self.hash)

