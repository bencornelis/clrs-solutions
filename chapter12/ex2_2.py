from tree_node import *

# Write recursive versions of TREE-MINIMUM and TREE-MAXIMUM.

def maximum(x):
    if x.right is None: return x
    return maximum(x.right)

def minimum(x):
    if x.left is None: return x
    return minimum(x.left)
