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
        else:
            self._recursiveInsert(self.root, new_node)

    def _recursiveInsert(self, node, new_node):
        if node.key > new_node.key:
            if node.leftChild is None:
                node.leftChild = new_node
                new_node.parent = node
            else:
                self._recursiveInsert(node.leftChild, new_node)
        else:
            if node.rightChild is None:
                node.rightChild = new_node
            else:
                self._recursiveInsert(node.rightChild, new_node)

    def search(self, key):
        if self.root is None:
            return False
        else:
            return self._recursiveSearch(self.root, key)

    def _recursiveSearch(self, node, key):
        if node.key == key:
            return True
        elif node.key > key:
            if node.leftChild is None:
                return False
            else:
                return self._recursiveSearch(node.leftChild, key)
        else:
            if node.rightChild is None:
                return False
            else:
                return self._recursiveSearch(node.rightChild, key)

class Node:
    def __init__(self, data=None, key=None):
        self.data = data
        self.key = key
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.height = 1
        self.size = 1