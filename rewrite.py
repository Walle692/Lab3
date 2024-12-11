from networkx.generators.classic import balanced_tree

from Node import Node

class BST:
    def __init__(self, c):
        self.root = None
        self.c = c

    def createNewBst(self, inorderlist):
        if len(inorderlist) == 0:
            return None
        mid = len(inorderlist) // 2
        root = inorderlist[mid]
        root.left = self.createNewBst(inorderlist[:mid])
        root.right = self.createNewBst(inorderlist[mid+1:])
        return root

    def insertPerfectBST(self, root):
        print("insertPerfectBST")
        newRoot = self.createPerfectBST(self.inorder(root))
        if root.parent is None:
            self.root = newRoot
            newRoot.parent = None
        else:
            newRoot.parent = root.parent
            if newRoot == root.parent.left:
                root.parent.left = newRoot
            else:
                root.parent.right = newRoot
        return newRoot


    def getroot(self):
        return self.root

    def updatesize(self, node):
        print("updatesize")
        if node is not None:
            node.update()
            while node.parent is not None:
                node = node.parent
                node.update()


    def insert(self, node):
        print("insert", node.key)
        root = self.root
        parent = None
        while root is not None:
            parent = root
            if node.key < root.key:
                root = root.left
            else:
                root = root.right
        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
        self.updatesize(node)

    def delete(self, node):
        print("delete")
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            replacement_node = self.minimum(node.right)
            if replacement_node != node.right:
                self.transplant(replacement_node, replacement_node.right)
                replacement_node.right = node.right
                replacement_node.right.parent = replacement_node
            self.transplant(node, replacement_node)
            replacement_node.left = node.left
            replacement_node.left.parent = replacement_node
            self.updatesize(replacement_node)
        self.updatesize(node)

    def transplant(self, to_be_replaced_node, replacement_node):
        print("transplant")
        if to_be_replaced_node.parent is None:
            self.root = replacement_node
        elif to_be_replaced_node == to_be_replaced_node.parent.left:
            to_be_replaced_node.parent.left = replacement_node
        else:
            to_be_replaced_node.parent.right = replacement_node
        if replacement_node is not None:
            replacement_node.parent = to_be_replaced_node.parent
        to_be_replaced_node.update()
        self.updatesize(to_be_replaced_node)


    def inorder(self, node):
        if node is not None:
            if node.left is not None:
                if node.right is not None:
                    return self.inorder(node.left) + [node] + self.inorder(node.right)
                return  self.inorder(node.left) + [node]
            if node.right is not None:
                return [node] + self.inorder(node.right)
            return [node]

    def search(self, root, key):
        if root is None or key == root.key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def minimum(self, root):
        while root.left is not None:
            root = root.left
        return root

    def maximum(self, root):
        while root.right is not None:
            root = root.right
        return root

    def successor(self, root):
        if root.right is not None:
            return self.minimum(root.right)
        else:
            parent = root.parent
            while parent is not None and root == parent.right:
                root = parent
                parent = root.parent
            return parent

