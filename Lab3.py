#
# Lab 3, D0012E
# Albin Täljsten, Linus Fridlund, Walter Wimmercranz
#
from random import randint
import time
from D_BST import *
from BinarySearchTree import BST
from Node import Node

def nodegenerator(tree, nodes):
    for i in range(0,nodes):
        newNode = Node( randint(0,4000),i)
        tree.insert(newNode)
    return tree, nodes

def superrandomnodegenerator(tree, nodes):
    nodekey_list = []
    for i in range(0,nodes):
        new_key = randint(0,100000000)
        if new_key not in nodekey_list:
            nodekey_list.append(new_key)
    for i in range(0,len(nodekey_list)):
        newNode = Node( randint(0,4000),nodekey_list[i])
        tree.insert(newNode)
    return tree, nodekey_list


def bst_tester(tree, nodes):
    tree, nodes = nodegenerator(tree, nodes)
    start_time = time.time()
    tree.search(nodes)
    search_time = time.time() - start_time
    node1 = Node("banana", nodes + 1)
    node2 = Node("apple", nodes + 2)
    node3 = Node("pear", nodes + 3)
    start_time = time.time()
    tree.insert(node1)
    tree.insert(node2)
    tree.insert(node3)
    insert_time = time.time() - start_time
    return search_time, insert_time



def main():
    bst1 = BST()
    d1   = D(0.5)

    bst2 = BST()
    d2 = D(0.75)

    bst3 = BST()
    d3 = D(1)




main()