
class MerkleTree():
    """
    Merkle tree is used for collecting and verifying transactions exist in a certain block.  
    """

    def __init__(self):
        self.root = None
        
    def add(self):
        pass

    def verify(self):
        pass

class MerkleNode():
    """
    Node of a merkle tree that contains the hash of either a transaction (Leaf node) or the hash of two other merkle nodes (non-leaf)
    """
    def __init__(self):
        self.leaf = False
        self.parent = None
        self.root = False
        self.hash = None
        self.children = []
