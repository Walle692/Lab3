#
# Lab 3, D0012E
# Albin Täljsten, Linus Fridlund, Walter Wimmercranz
#
from random import randint

from BinarySearchTree import BST
from Node import Node

def nodegenerator(tree):
    for i in range(0,10):
        newNode = Node( randint(0,4000),i)
        tree.insert(newNode)
    return tree

def main():
    tree = BST(0.5)
    nodegenerator(tree)
    tree.leveltraverse(tree.getroot())
    print(tree.inorder(tree.getroot()))
    #print(type(tree.inorder(tree.getroot())))
    #for Node in tree.inorder(tree.getroot()):
        #print(Node.key)
    #print(tree.createPerfectBST(tree.inorder(tree.getroot())).size)
    #perfectroot = tree.createPerfectBST(tree.inorder(tree.getroot()))
    #print(perfectroot.key, perfectroot.left.key, perfectroot.right.key)


main()