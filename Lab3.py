#
# Lab 3, D0012E
# Albin Täljsten, Linus Fridlund, Walter Wimmercranz
#
from random import randint
import sys
import time
from D_BST import *
from BinarySearchTree import BST
from Node import Node

sys.setrecursionlimit(100006)

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
    start_time = time.time()
    tree, nodes = nodegenerator(tree, nodes)
    insert_time = time.time() - start_time
    start_time = time.time()
    tree.search(tree.getroot(), nodes)
    search_time = time.time() - start_time
    return search_time, insert_time

def bst_tester2(tree, nodes):
    tree, nodes = superrandomnodegenerator(tree, nodes)
    start_time = time.time()
    tree.search(tree.getroot(), nodes)
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


    nodes_to_run = [100, 1000, 5000, 10000, 15000, 20000]
    for integers in nodes_to_run:
        bst1 = BST()
        d1 = D(0.55)
        d2 = D(0.65)
        d3 = D(0.75)
        d4 = D(0.85)
        d5 = D(0.95)
        search_time_bst1, insert_time_bst1 = bst_tester(bst1, integers)
        print("BST, nodes: ", integers, " search time: ", search_time_bst1," insertion time: ", insert_time_bst1)
        search_time_d1, insert_time_d1 = bst_tester(d1, integers)
        print("D(0.55), nodes: ", integers, " search time: ", search_time_d1," insertion time: ", insert_time_d1)
        search_time_d2, insert_time_d2 = bst_tester(d2, integers)
        print("D(0.65), nodes: ", integers, " search time: ", search_time_d2," insertion time: ", insert_time_d2)
        search_time_d3, insert_time_d3 = bst_tester(d3, integers)
        print("D(0.75), nodes: ", integers, " search time: ", search_time_d3," insertion time: ", insert_time_d3)
        search_time_d4, insert_time_d4 = bst_tester(d4, integers)
        print("D(0.85), nodes: ", integers, " search time: ", search_time_d4," insertion time: ", insert_time_d4)
        search_time_d5, insert_time_d5 = bst_tester(d5, integers)
        print("D(0.95), nodes: ", integers, " search time: ", search_time_d5," insertion time: ", insert_time_d5)
        del bst1
        del d1
        del d2
        del d3
        del d4
        del d5







main()