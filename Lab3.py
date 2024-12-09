#
# Lab 3, D0012E
# Albin Täljsten, Linus Fridlund, Walter Wimmercranz
#
from BinarySearchTree import BST
from Node import Node


def main():
    tree = BST()
    testnode = Node(3, 11)
    tree.insert(testnode)
    tree.insert(Node("senap", 10))
    print(tree.getroot().size)
    tree.insert(Node("kanin", 12))
    print(tree.getroot().size)
    tree.insert(Node("katt", 9))
    print(tree.getroot().size)
    linus_node = Node("linus", 8)
    tree.insert(linus_node)
    print(tree.inorder(tree.getroot()))
    print(tree.getroot().size)
    tree.delete(testnode)
    print(tree.inorder(tree.getroot()))
    print(tree.getroot().size)
    


main()