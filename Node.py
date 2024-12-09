class Node:
    def __init__(self, data=None, key=None):
        self.data = data
        self.key = key
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.height = 1
        self.size = 1
