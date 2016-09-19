from construct_tree import *

# Write an O(n)-time nonrecursive procedure that, given an n-node binary tree,
# prints out the key of each node. Use no more than constant extra space outside
# of the tree itself and do not modify the tree, even temporarily, during the procedure.

def print_tree(root):
    """
    Prints the keys of the nodes in a binary tree.

    >>> root = construct_tree([4,3,9,None,2,1,5,None,None,8,7,None,6,None,10])
    >>> print_tree(root)
    4
    3
    2
    8
    7
    9
    1
    6
    5
    10

    """
    node = root
    while True:
        print(node.key)
        if node.left:
            node = node.left
        elif node.right:
            node = node.right
        else:
            while no_right_sibling(node):
                node = node.p
            if node == root:
                return
            node = node.p.right

def no_right_sibling(node):
    return node.p and (node.p.right == node or node.p.right is None)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
