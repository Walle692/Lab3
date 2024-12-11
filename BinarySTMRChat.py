from Node import Node


class BST:
    def __init__(self, c):
        """
        Initialize the Binary Search Tree (BST).
        :param c: Balancing factor for tree rebalancing conditions.
        """
        self.root = None  # The root node of the tree.
        self.c = c  # Balancing factor.

    def createPerfectBST(self, nodeList):
        """
        Create a perfectly balanced BST from a sorted list of nodes.
        :param nodeList: List of nodes (sorted by key).
        :return: Root of the balanced BST.
        """
        if len(nodeList) == 0:
            return None

        mid = len(nodeList) // 2
        root = nodeList[mid]

        # Recursively build the left and right subtrees
        root.left = self.createPerfectBST(nodeList[:mid])
        root.right = self.createPerfectBST(nodeList[mid + 1:])

        # Update parent references
        if root.left is not None:
            root.left.parent = root
        if root.right is not None:
            root.right.parent = root

        # Update size and other properties of the root
        root.update()
        return root

    def insertPerfectBST(self, root):
        """
        Rebuild the subtree rooted at the given node as a perfect BST.
        :param root: The root of the subtree to rebuild.
        :return: The new root of the rebuilt subtree.
        """
        nodeList = self.inorder(root)  # Get all nodes in sorted order
        newRoot = self.createPerfectBST(nodeList)

        # Update parent references
        if root.parent is None:
            self.root = newRoot
            newRoot.parent = None
        else:
            newRoot.parent = root.parent
            if root == root.parent.left:
                root.parent.left = newRoot
            else:
                root.parent.right = newRoot

        return newRoot

    def getroot(self):
        """
        Get the root of the BST.
        :return: The root node.
        """
        return self.root

    def updatesize(self, node):
        """
        Update the sizes and rebalance the tree if necessary.
        :param node: The node from where the update starts.
        """
        while node is not None:
            node.update()

            # Check balance conditions
            if node.left and node.right:
                if node.left.size > self.c * node.right.size or node.right.size > self.c * node.left.size:
                    node = self.insertPerfectBST(node)
            elif node.left and node.left.size > 1:
                node = self.insertPerfectBST(node)
            elif node.right and node.right.size > 1:
                node = self.insertPerfectBST(node)

            node = node.parent

    def insert(self, node):
        """
        Insert a node into the BST.
        :param node: The node to insert.
        """
        parent = None
        current = self.root

        # Find the appropriate position for the new node
        while current is not None:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        # Attach the new node to the tree
        node.parent = parent
        if parent is None:
            self.root = node  # Tree was empty, new node is the root
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        # Update sizes and rebalance
        self.updatesize(node)

    def delete(self, node):
        """
        Delete a node from the BST.
        :param node: The node to delete.
        """
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            replacement = self.minimum(node.right)

            if replacement.parent != node:
                self.transplant(replacement, replacement.right)
                replacement.right = node.right
                replacement.right.parent = replacement

            self.transplant(node, replacement)
            replacement.left = node.left
            replacement.left.parent = replacement

        self.updatesize(node)

    def transplant(self, to_replace, replacement):
        """
        Replace one subtree with another.
        :param to_replace: The subtree to replace.
        :param replacement: The new subtree.
        """
        if to_replace.parent is None:
            self.root = replacement
        elif to_replace == to_replace.parent.left:
            to_replace.parent.left = replacement
        else:
            to_replace.parent.right = replacement

        if replacement is not None:
            replacement.parent = to_replace.parent

    def inorder(self, node):
        """
        Perform an inorder traversal of the BST.
        :param node: The starting node.
        :return: List of nodes in inorder.
        """
        if node is None:
            return []
        return self.inorder(node.left) + [node] + self.inorder(node.right)

    def search(self, root, key):
        """
        Search for a node with a specific key.
        :param root: The root node of the subtree.
        :param key: The key to search for.
        :return: The node with the given key, or None if not found.
        """
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def minimum(self, root):
        """
        Find the node with the smallest key in the subtree.
        :param root: The root of the subtree.
        :return: The node with the smallest key.
        """
        while root.left is not None:
            root = root.left
        return root

    def maximum(self, root):
        """
        Find the node with the largest key in the subtree.
        :param root: The root of the subtree.
        :return: The node with the largest key.
        """
        while root.right is not None:
            root = root.right
        return root

    def successor(self, root):
        """
        Find the successor of a given node.
        :param root: The node to find the successor for.
        :return: The successor node, or None if there is no successor.
        """
        if root.right is not None:
            return self.minimum(root.right)

        parent = root.parent
        while parent is not None and root == parent.right:
            root = parent
            parent = root.parent
        return parent

    def leveltraverse(self, root):
        """
        Perform a level-order traversal of the BST.
        :param root: The root of the tree.
        """
        if root is None:
            return

        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            print(f"Node: {node.key}, Level: {level}")

            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))
