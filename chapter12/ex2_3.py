from operations import *

# Write the TREE-PREDECESSOR procedure.

def predecessor(x):
    if x.left:
        return maximum(x.left)
    else:
        y = x.p
        while y is not None and y.left == x:
            x = y
            y = x.p
        return y
