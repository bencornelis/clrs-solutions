from linked_list import *

# Give a O(n)-time nonrecursive procedure that reverses a singly linked list of n
# elements. The procedure should use no more than constant storage beyond that
# needed for the list itself

def reverse(l):
    """
    Return a singly linked list of n elements in reverse order.

    >>> l = LinkedList()
    >>> l.head = Node(5)
    >>> l.head.next = Node(6)
    >>> l.head.next.next = Node(7)
    >>> rl = reverse(l)
    >>> rl.head.key
    7
    >>> rl.head.next.key
    6
    >>> rl.head.next.next.key
    5

    """
    prev = l.head
    cur = l.head.next

    while cur is not None:
        nxt = cur.next
        cur.next = prev

        prev = cur
        cur = nxt

    l.head = prev
    return l

if __name__ == "__main__":
    import doctest
    doctest.testmod()
