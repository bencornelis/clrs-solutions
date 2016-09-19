from binary_tree import *
from stack import *

# Write an O(n)-time nonrecursive procedure that, given an n-node binary tree,
# prints out the key of each node in the tree. Use a stack as an auxiliary data structure

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
    stack = Stack()
    stack.push(root)

    while not stack.is_empty():
        node = stack.pop()
        print(node.key)

        if node.right is not None:
            stack.push(node.right)
        if node.left is not None:
            stack.push(node.left)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
