from tree_node import *

# Write an O(n)-time recursive procedure that, given an n-node binary tree, prints
# out the key of each node in the tree.

def print_tree(root):
    """
    Prints the keys of the nodes in a binary tree.

    >>> root = Node(1)
    >>> root.left = Node(2)
    >>> root.right = Node(3)
    >>> root.left.right = Node(4)
    >>> root.left.right.left = Node(5)
    >>> root.left.right.right = Node(6)
    >>> print_tree(root)
    1
    2
    4
    5
    6
    3

    """
    if root is None: return
    print(root.key)
    print_tree(root.left)
    print_tree(root.right)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
