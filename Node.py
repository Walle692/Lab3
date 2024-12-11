class Node:

    def __init__(self, data=None, key=None):
        self.data = data
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.c = 1
        self.size = 1

    def update(self):
        if self.left is not None and self.right is not None:
            self.size = ( self.left.size + self.right.size + 1)
        elif self.left is not None and self.right is None:
            self.size = (self.left.size + 1)
        elif self.left is None and self.right is not None:
            self.size = (self.right.size + 1)
        else:
            self.size = 1