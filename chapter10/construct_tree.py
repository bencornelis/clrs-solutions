from tree_node import *

def construct_tree(keys):
    """
    Return root of tree constructed from list of keys.

    >>> root = construct_tree([4,3,9,None,2,1,5,None,None,8,7,None,6,None,10])
    >>> level0 = [root]
    >>> level1 = [root.left, root.right]
    >>> level2 = [root.left.right, root.right.left, root.right.right]
    >>> level3 = [root.left.right.left, root.left.right.right, root.right.left.right, root.right.right.right]
    >>> get_key = lambda node: node.key
    >>> get_level_keys = lambda level: map(get_key, level)
    >>> map(get_level_keys, [level0, level1, level2, level3])
    [[4], [3, 9], [2, 1, 5], [8, 7, 6, 10]]

    """
    nodes = map(lambda k: Node(k) if k else None, keys)
    nodes.insert(0, None) # for better indexing
    n = len(nodes)

    for i in range(1, n):
        node = nodes[i]
        if node is None:
            continue
        else:
            node.p     = nodes[i/2]
            node.left  = nodes[2*i]     if 2*i < n     else None
            node.right = nodes[2*i + 1] if 2*i + 1 < n else None

    return nodes[1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
