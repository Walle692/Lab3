#
# Lab 3, D0012E
# Albin Täljsten, Linus Fridlund, Walter Wimmercranz
#
from BinarySearchTree import BST
from Node import Node


def main():
    tree = BST
    node = Node("senap", 10)
    tree.insert(node)
    tree.insert(Node("kanin", 12))
    tree.insert(Node("katt", 9))

    


main()