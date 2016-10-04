from tree_node import *

# Give recursive algorithms that perform preorder and postorder tree walks in O(n)
# time on a tree of n nodes.

def preorder_tree_walk(x):
    if x:
        print(x.key)
        preorder_tree_walk(x.left)
        preorder_tree_walk(x.right)

def postorder_tree_walk(x):
    if x:
        preorder_tree_walk(x.left)
        preorder_tree_walk(x.right)
        print(x.key)
