def inorder_tree_walk(x):
    """
    Print the keys of binary search tree in sorted order.
    """
    if x:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)
