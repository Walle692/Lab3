#
# Lab 3, D0012E
# Albin Täljsten, Linus Fridlund, Walter Wimmercranz
#

class binarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data, key):
        new_node = Node(data, key)
        if self.root is None:
            self.root = new_node

        if self.root.key > key:
            if self.root.leftChild is None:
                self.root.leftChild = new_node
                new_node.parent = self.root
            else:
                self.root.leftChild.insert(data, key)
        else:
            if self.root.rightChild is None:
                self.root.rightChild = new_node
                new_node.parent = self.root
            else:
                self.root.rightChild.insert(data, key)

class Node:
    def __init__(self, data=None, key=None):
        self.data = data
        self.key = key
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.height = 1
        self.size = 1