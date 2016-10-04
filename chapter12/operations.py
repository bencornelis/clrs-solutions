from tree_node import *

# O(h) running time, where h is the height of the tree
def maximum(x):
    """ Returns the maximum node in a tree rooted at x. """
    while x.right:
        x = x.right
    return x

# O(h) running time
def minimum(x):
    while x.left:
        x = x.left
    return x

def successor(x):
    if x.right:
        return minimum(x.right)
    else:
        y = x.p
        while y is not None and y.right == x:
            x = y
            y = x.p
        return y

def search(x, k):
    while x is not None and x.key != k:
        if k < k.key:
            x = x.left
        else:
            x = x.right
    return x

def insert(x, z):
    """ Insert z into tree rooted at x. """
    while x:
        y = x
        if z.key <= x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if z.key <= y.key:
        y.left = z
    else:
        y.right = z
    return x

def transplant(x, u, v):
    """ Transplants subtree at v to subtree at u in tree rooted at x. """
    if u.p is None:         # u is the root
        return v
    else if u.p.right == u: # u is the right child of its parent
        u.p.right = v
    else:                   # u is the left child of its parent
        u.p.left = v
    if v:
        v.p = u.p
    return x

def delete(x):
    """ Delete z from tree rooted at x. """
    if z.left is None:
        return transplant(x, z, z.right)
    else if z.right is None:
        return transplant(x, z, z.left)
    else: # replace z with its predecessor
        m = maximum(z.left)
        if m.p != z:
            x = transplant(x, m, m.left)
            m.left = z.left
            m.left.p = m
        m.right = z.right
        m.right.p = m
        m.p = z.p
        return x
