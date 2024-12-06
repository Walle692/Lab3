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

    def delete(self, key):
        if self.root is None:
            return None
        else:
            return self._recursiveDelete(self.root, key)

    def _recursiveDelete(self, node, key):
        if node.key == key:
            if node.leftChild is None and node.rightChild is None:
                return self._nodeIsLeafDelete(node)
            elif node.leftChild is None and node.rightChild is not None:
                return self._nodeHasOneChild(node)
            elif node.leftChild is not None and node.rightChild is None:
                return self._nodeHasOneChild(node)
            else:
                return self._nodeHasTwoChildren(node)
        elif node.key > key:
            if node.leftChild is None:
                return None
            else:
                return self._recursiveDelete(node.leftChild, key)
        else:
            if node.rightChild is None:
                return False
            else:
                return self._recursiveDelete(node.rightChild, key)

    def _nodeIsLeafDelete(self, node):
        if self.root == node:
            self.root = None
        elif node.parent.leftChild == node:
            node.parent.leftChild = None
            node.parent = None
        elif node.parent.rightChild == node:
            node.parent.rightChild = None
            node.parent = None
        return node

    def _nodeHasOneChild(self, node):
        if node.leftChild is not None:
            if node.parent.leftChild == node:
                node.parent.leftChild = node.leftChild
                node.leftChild.parent = node.parent
            else:
                node.parent.rightChild = node.leftChild
                node.leftChild.parent = node.parent
        else:
            if node.parent.leftChild == node:
                node.parent.leftChild = node.rightChild
                node.rightChild.parent = node.parent
            else:
                node.parent.rightChild = node.rightChild
                node.rightChild.parent = node.parent
        return node

    def _nodeHasTwoChildren(self, node):
        replacement = self._findleftmin(node.rightChild)
        self.delete(replacement.key)
        replacement.rightChild = node.rightChild
        replacement.rightChild.parent = replacement
        replacement.leftChild = node.leftChild
        replacement.leftChild.parent = replacement
        replacement.parent = node.parent
        if replacement.parent.leftChild == node:
            replacement.parent.leftChild = replacement
        else:
            replacement.parent.rightChild = replacement
        return node

    def _findleftmin(self, node):
        while node.leftChild is not None:
            node = node.leftChild
        return node

    def printTree(self):
        


class Node:
    def __init__(self, data=None, key=None):
        self.data = data
        self.key = key
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.height = 1
        self.size = 1

def main():
    tree = binarySearchTree()
    tree.insert(10, 10)
    tree.insert(5, 5)
    tree.insert(15, 6)
    tree.insert(2, 2)
    tree.insert(1,20)
    tree.insert(11, 11)
    tree.printTree()


main()