from Node import Node

class BST:
    def __init__(self, c):
        self.root = None
        self.c = c

    def createPerfectBST(self, nodeList):
        if len(nodeList) == 0:
            return None
        mid = len(nodeList) // 2
        original = nodeList[mid]
        root = Node(original.data, original.key)
        root.left = self.createPerfectBST(nodeList[:mid])
        root.right = self.createPerfectBST(nodeList[mid+1:])
        if root.left is not None:
            root.left.parent = root
        if root.right is not None:
            root.right.parent = root
        root.update()
        return root

    #
    def insertPerfectBST(self, root):
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

    #returns root of tree
    def getroot(self):
        return self.root

    #update size for node and its parents
    def updatesize(self, node):
        if node is not None:
            node.update()
            if self.updatechecker(node):
                node = self.insertPerfectBST(node)
            while node.parent is not None:
                node = node.parent
                if self.updatechecker(node):
                    node = self.insertPerfectBST(node)
                node.update()

    #check if size conditions, are fulfilled
    def updatechecker(self, node):
        if node.left is not None and node.right is not None:
            if node.left.size > self.c * node.right.size:
                return True
            elif node.right.size > self.c * node.left.size:
                return True
        elif node.left is not None and node.right is None:
            if node.left.size > 1:
                return True
        elif node.right is not None and node.left is None:
            if node.right.size > 1:
                return True
        return False

    #insert node
    def insert(self, node):
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

    #delete node
    def delete(self, node):
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

    #replace node with another node
    def transplant(self, to_be_replaced_node, replacement_node):
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

    #Create list of Nodes, from smallest key to largest
    def inorder(self, node):
        if node is not None:
            if node.left is not None:
                if node.right is not None:
                    return self.inorder(node.left) + [node] + self.inorder(node.right)
                return  self.inorder(node.left) + [node]
            if node.right is not None:
                return [node] + self.inorder(node.right)
            return [node]

    #search for key, from selected root
    def search(self, root, key):
        if root is None or key == root.key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # look for minimum from inputed root by going as far left as possible
    def minimum(self, root):
        while root.left is not None:
            root = root.left
        return root

    #look for maximum from inputed root by going as far right as possible
    def maximum(self, root):
        while root.right is not None:
            root = root.right
        return root

    #get the node with the closest key to input node
    def successor(self, root):
        if root.right is not None:
            return self.minimum(root.right)
        else:
            parent = root.parent
            while parent is not None and root == parent.right:
                root = parent
                parent = root.parent
            return parent

    def leveltraverse(self, root):
        if root is None:                                                    #Breadth search first
            return []
        queue = [(root,0)]                                                  #Create queue
        while len(queue) > 0:
            print("key :" ,queue[0][0].key, "level :", queue[0][1])
            tuple = queue.pop(0)
            node = tuple[0]                                                 #get current node
            level = tuple[1] + 1
            if node.left is not None:
                queue.append((node.left, level))                            #add node:s children to queue
            if node.right is not None:
                queue.append((node.right, level))